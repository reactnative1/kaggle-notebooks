# 🤖 HyperFlow H3 Flash Ref2VA (Headless Mode)

Autonomous, end-to-end batch generation pipeline designed for AI agents (Antigravity) and headless execution on Kaggle Dual Nvidia Tesla T4 GPUs.

---

## ⚡ Specifications

* **Model:** `VideoRebirthAI/hyperflow-h3-flash` (ref2va_int8_convrot_comfyui)
* **Mode:** **Autonomous Headless Batch Runner**
* **Accelerator:** Kaggle Dual Nvidia Tesla T4 GPU (or P100)
* **Execution:** Direct REST API queue execution through headless ComfyUI

---

## 🛡️ Fault Tolerance & Quota Features

1. **Option 1 Batch Configuration:** Prompts, seeds, and reference files are defined in Cell 1 (`BATCH_JOBS = [...]`). The agent can customize this cell programmatically before pushing.
2. **Non-Blocking Error Handling:** Each batch item is isolated in a `try...except` block. If one prompt fails, it logs the error and immediately proceeds to the next shot without aborting the batch.
3. **Immediate Output Streaming:** Finished outputs are written to `/kaggle/working/outputs/` the instant they are rendered.
4. **Auto-Termination on Completion:** Once all batch jobs are processed, the runner prints a detailed summary and immediately calls `sys.exit(0)` to stop the kernel, burning **zero idle GPU quota**.

---

## 🚀 How to Run

### Via Local Push Dispatcher
```bash
# Push with your active profile
python tools/push_kernel.py workflows/hyperflow-h3-flash_headless_mode

# Or specify a profile and attach the weights dataset
python tools/push_kernel.py workflows/hyperflow-h3-flash_headless_mode --profile my_profile -d my_username/minimax-h3-open-weights
```
