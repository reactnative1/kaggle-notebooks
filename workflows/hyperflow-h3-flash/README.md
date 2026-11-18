# 🎬 HyperFlow H3 Flash Ref2VA Studio

Production workflow for fast Joint Video & Audio Reference Generation using **MiniMax H3 Flash LoRA** on Kaggle Dual Nvidia Tesla T4 GPUs.

---

## ⚡ Specifications

* **Model:** `VideoRebirthAI/hyperflow-h3-flash` (ref2va_int8_convrot_comfyui)
* **Checkpoints:**
  * Transformer: `minimax_h3_ref2va_hyperflow_flash_14b-int8_convrot.safetensors` (~15.3 GB)
  * Text/Vision Encoder: `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` (~14.6 GB)
  * Video VAE: `minimax_h3_video_vae_int8_convrot.safetensors`
  * Audio VAE: `minimax_h3_audio_vae_fp32.safetensors`
* **Accelerator:** Kaggle Dual Nvidia Tesla T4 GPU (or P100)
* **Runtime:** Headless ComfyUI API + live Cloudflare monitoring tunnel

---

## 📦 Dataset & Weight Caching

* **Attached Dataset:** `minimax-h3-open-weights` (Auto-detected if mounted, for 0-second instant startup).
* **Automatic Fallback:** If the dataset is not mounted, the notebook automatically downloads the weights directly from Hugging Face via multi-threaded `hf_transfer`.

---

## 🚀 How to Run

### Option 1: One-Click Local Dispatch (Zero Account Exposure)
Push to whichever Kaggle account you want using the local dispatcher:
```bash
# Push using Account Profile A
python tools/push_kernel.py workflows/hyperflow-h3-flash --profile profile_a

# Or push using Account Profile B (runs on that account's GPU quota)
python tools/push_kernel.py workflows/hyperflow-h3-flash --profile profile_b
```

### Option 2: Run via Kaggle Web Editor
1. Create a new notebook on [Kaggle](https://www.kaggle.com/code).
2. Attach GPU (`Nvidia Tesla T4`).
3. Click **File -> Upload Notebook** and select `notebook.ipynb`.
4. (Optional for speed) Click **+ Add Input**, search for `minimax-h3-open-weights`, and click **Add**.
5. Click **Run All**.
