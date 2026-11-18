# 🤖 LongCat Video Avatar 1.6 INT8 (Headless Batch Mode)

Autonomous, end-to-end batch generation pipeline designed for AI agents (Antigravity) and headless execution on Kaggle Dual Nvidia Tesla T4 GPUs.

---

## ⚡ Specifications

* **Model:** `meituan-longcat/LongCat-Video-Avatar-1.6` & `TeamAIQ/LongCat-Video-Avatar-1.6-INT8-ConvRot`
* **Mode:** **Autonomous Headless Batch Runner**
* **Accelerator:** Kaggle Dual Nvidia Tesla T4 GPU (`accelerator: NvidiaTeslaT4`)
* **Execution:** Direct Python inference execution with zero web server overhead
* **Data Sources:** Pre-mounted Kaggle Dataset (`nizamamzn/longcat-avatar-weights`) with 0s instant symlinking + automatic Hugging Face fallback

---

## 🛡️ Fault Tolerance & Quota Features

1. **Option 1 Batch Configuration:** Prompts, reference portraits, and audio files can be defined programmatically before pushing.
2. **Immediate Output Delivery:** Rendered MP4 videos are written directly to `/kaggle/working/outputs/`.
3. **Auto-Termination on Completion:** Once the batch generation finishes, the runner exits cleanly with `sys.exit(0)`, saving the output video to Kaggle kernel files and burning **zero idle GPU quota**.

---

## 🚀 How to Run

### Via Local Push Dispatcher
```bash
# Push with your active profile and attached weights dataset
python tools/push_kernel.py runners/longcat-video-avatar_headless_mode --profile my_profile -d nizamamzn/longcat-avatar-weights
```
