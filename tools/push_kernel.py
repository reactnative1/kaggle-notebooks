#!/usr/bin/env python3
"""
Kaggle Notebooks Dispatcher (Zero Account Leaks)

Reads an account-agnostic `config.json` inside a workflow folder, dynamically
injects the active Kaggle username from local credentials or selected profile,
generates a temporary `kernel-metadata.json`, and pushes the kernel.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

def resolve_kaggle_username(config_dir: Path) -> str:
    kaggle_json_path = config_dir / "kaggle.json"
    if not kaggle_json_path.exists():
        raise FileNotFoundError(f"Could not find kaggle.json at {kaggle_json_path}")
    with open(kaggle_json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    username = data.get("username")
    if not username:
        raise ValueError(f"No 'username' field found in {kaggle_json_path}")
    return username

def main():
    parser = argparse.ArgumentParser(description="Push a generic workflow notebook to Kaggle.")
    parser.add_argument("workflow_dir", type=str, help="Path to workflow folder containing config.json")
    parser.add_argument("--profile", "-p", type=str, default=None, help="Profile name in ~/.kaggle/profiles/<profile>")
    parser.add_argument("--dataset", "-d", action="append", default=[], help="Attach dataset source(s) (e.g. -d username/dataset-slug)")
    parser.add_argument("--dry-run", action="store_true", help="Print generated metadata without pushing")
    parser.add_argument("--keep-metadata", action="store_true", help="Keep generated kernel-metadata.json after pushing")
    args = parser.parse_args()

    wf_dir = Path(args.workflow_dir).resolve()
    config_file = wf_dir / "config.json"

    if not config_file.exists():
        print(f"Error: No config.json found in {wf_dir}", file=sys.stderr)
        sys.exit(1)

    with open(config_file, "r", encoding="utf-8") as f:
        config = json.load(f)

    # Determine Kaggle config directory
    env = os.environ.copy()
    if args.profile:
        profiles_dir = Path.home() / ".kaggle" / "profiles" / args.profile
        if not profiles_dir.exists():
            print(f"Error: Profile directory not found: {profiles_dir}", file=sys.stderr)
            sys.exit(1)
        config_dir = profiles_dir
        env["KAGGLE_CONFIG_DIR"] = str(profiles_dir)
    elif "KAGGLE_CONFIG_DIR" in env:
        config_dir = Path(env["KAGGLE_CONFIG_DIR"])
    else:
        config_dir = Path.home() / ".kaggle"

    username = resolve_kaggle_username(config_dir)
    slug = config.get("slug")
    if not slug:
        print("Error: 'slug' must be defined in config.json", file=sys.stderr)
        sys.exit(1)

    kernel_id = f"{username}/{slug}"
    print(f">>> Target Kaggle Identity: {username} (via {config_dir.name})")
    print(f">>> Target Kernel ID:       {kernel_id}")
    print(f">>> Pushing from:           {wf_dir}")

    # Merge datasets from config and CLI arguments
    datasets = list(config.get("dataset_sources", []))
    for d in args.dataset:
        if d not in datasets:
            datasets.append(d)

    # Build Kaggle metadata dictionary
    metadata = {
        "id": kernel_id,
        "title": config.get("title", slug.replace("-", " ").title()),
        "code_file": config.get("code_file", "notebook.ipynb"),
        "language": config.get("language", "python"),
        "kernel_type": config.get("kernel_type", "notebook"),
        "is_private": config.get("is_private", True),
        "enable_gpu": config.get("enable_gpu", True),
        "enable_tpu": config.get("enable_tpu", False),
        "enable_internet": config.get("enable_internet", True),
        "dataset_sources": datasets,
        "competition_sources": config.get("competition_sources", []),
        "kernel_sources": config.get("kernel_sources", []),
        "model_sources": config.get("model_sources", []),
        "accelerator": config.get("accelerator", "NvidiaTeslaT4")
    }

    meta_file = wf_dir / "kernel-metadata.json"
    if args.dry_run:
        print("\n[DRY RUN] Generated kernel-metadata.json content:")
        print(json.dumps(metadata, indent=2))
        return

    with open(meta_file, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    try:
        cmd = [sys.executable, "-m", "kaggle", "kernels", "push", "-p", str(wf_dir)]
        subprocess.run(cmd, env=env, check=True)
        print(f"\n[OK] Kernel pushed successfully to https://www.kaggle.com/code/{kernel_id}")
    finally:
        if not args.keep-metadata and meta_file.exists():
            meta_file.unlink()

if __name__ == "__main__":
    main()
