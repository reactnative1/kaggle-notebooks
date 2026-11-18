# 🎤 LongCat Video Avatar 1.6 INT8 (Interactive Human Mode)

Interactive, browser-based cloud runner for lip-synced talking & singing avatar video generation using **LongCat-Video-Avatar 1.6 INT8** with Tensor-Parallel DiT on Kaggle Dual Nvidia Tesla T4 GPUs.

---

## ⚡ Specifications

* **Model:** `meituan-longcat/LongCat-Video-Avatar-1.6` & `TeamAIQ/LongCat-Video-Avatar-1.6-INT8-ConvRot`
* **Mode:** **Interactive Human Web UI**
* **Accelerator:** Kaggle Dual Nvidia Tesla T4 GPU (`accelerator: NvidiaTeslaT4`)
* **Interface:** Gradio 5.29 UI with Cloudflare Public Tunnel & Gradio Share links
* **Data Sources:** Pre-mounted Kaggle Dataset (`nizamamzn/longcat-avatar-weights`) with 0s instant symlinking + automatic Hugging Face fallback

---

## 🚀 How to Run

### Option 1: Via Kaggle Web Editor (One-Click)
1. Download or open `notebook.ipynb`.
2. Create a new notebook on [Kaggle](https://www.kaggle.com/code) and upload `notebook.ipynb`.
3. In **Data**, click **Add Data** and search for `nizamamzn/longcat-avatar-weights` to attach the weights (enables 0s instant mount).
4. In **Settings**, set **Accelerator: GPU T4 x2** and **Internet: On**.
5. Run all cells. Step 2 will output a public Cloudflare link (`https://....trycloudflare.com`) and Gradio share link.
6. Open the link to upload your character portrait and speech/song audio!

### Option 2: Via Local Push Dispatcher
```bash
python tools/push_kernel.py runners/longcat-video-avatar --profile my_profile -d nizamamzn/longcat-avatar-weights
```
*(The server will remain online so you can interact with the web interface until you stop the session).*
