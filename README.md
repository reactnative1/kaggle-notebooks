# ⚡ AI Kaggle Cloud Notebooks

A modular, production-ready repository of generative AI workflows, cloud GPU runners, and studio pipelines optimized for **Kaggle Cloud GPUs (Dual Nvidia Tesla T4 / P100)**.

---

## 🔒 Security & Privacy Standard: Zero Account Leaks

This repository is **strictly account-agnostic and public-safe**:
* **No Hardcoded Usernames or Identifiers:** No account names or personal emails are stored in any notebook or config.
* **No Credentials:** `kernel-metadata.json` and credentials are strictly `.gitignore`d.
* **Dynamic Local Dispatch:** A generic local tool injects your active local Kaggle profile at push time without modifying or committing files.
* **Cross-Account Quota Ready:** Write your code once, commit once to Git, and push to whichever account has available GPU quota.

---

## 📋 Catalog of Workflows

| Category | Workflow | Hardware | Description | Guide |
| :--- | :--- | :--- | :--- | :--- |
| **Video & Audio** | `hyperflow-h3-flash` | Dual Nvidia Tesla T4 | Fast joint video & audio generation with MiniMax H3 Flash LoRA (Ref2VA INT8) | [README](workflows/hyperflow-h3-flash/README.md) |
| **Audio / TTS** | `qwen3-tts-studio` *(Upcoming)* | Single T4 / P100 | High-fidelity voice cloning, paced dialogue synthesis, and voice design | *(Next)* |
| **Video Enhancement** | `minimax-h3-face-restoration` *(Upcoming)* | Dual Nvidia Tesla T4 | ComfyUI wide-shot facial restoration pipeline using VoSR2 & SAM | *(Next)* |

---

## 🚀 Quickstart: Local Push Dispatcher

Push any workflow directly to Kaggle using your local profile without touching Git:

```bash
# 1. Push to your active Kaggle account
python tools/push_kernel.py workflows/hyperflow-h3-flash

# 2. Or specify a local profile (~/.kaggle/profiles/<profile_name>)
python tools/push_kernel.py workflows/hyperflow-h3-flash --profile my_account
```

---

## 🌐 Running Manually in the Kaggle Web UI

1. Open [Kaggle Notebooks](https://www.kaggle.com/code) and click **New Notebook**.
2. Go to **File -> Upload Notebook** and select the `notebook.ipynb` from the target workflow folder.
3. In the right panel, select **Accelerator: GPU T4 x2** (or **P100**) and enable **Internet On**.
4. Click **Run All**.
