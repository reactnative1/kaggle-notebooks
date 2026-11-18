# 🤖 Qwen3-TTS 1.7B (Headless Mode)

Autonomous, end-to-end batch dialogue synthesis pipeline for AI agents (Antigravity) on Kaggle Cloud GPU.

---

## ⚡ Specifications

* **Models:** `Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign`
* **Mode:** **Autonomous Headless Batch Runner**
* **Accelerator:** Kaggle Single or Dual Nvidia Tesla T4 GPU (or P100)
* **Mastering:** Automated broadcast loudness normalization (`-14 LUFS`)

---

## 🛡️ Fault Tolerance & Quota Features

1. **Option 1 Batch Configuration:** Dialogues, pacing marks, and voice descriptions are defined in Cell 1 (`BATCH_DIALOGUES = [...]`). The agent can customize this cell programmatically before dispatching.
2. **Non-Blocking Error Handling:** Each dialogue runs in an isolated `try...except` block. If one line encounters an issue, it logs the error and proceeds immediately to the next dialogue.
3. **Immediate Audio Persistence:** Mastered WAV files are written directly to `/kaggle/working/outputs/` as each line finishes.
4. **Auto-Termination on Completion:** Once all dialogues are rendered, the runner calls `sys.exit(0)` to stop the kernel, burning **zero idle GPU quota**.

---

## 🚀 How to Run

### Via Local Push Dispatcher
```bash
python tools/push_kernel.py runners/qwen3-tts-studio_headless_mode --profile my_profile
```
