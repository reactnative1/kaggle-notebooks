# 🎬 HyperFlow H3 Flash Ref2VA Studio (Interactive Human Mode)

Interactive, browser-based workflow for joint video & audio reference generation using **MiniMax H3 Flash LoRA** on Kaggle Dual Nvidia Tesla T4 GPUs.

---

## ⚡ Specifications

* **Model:** `VideoRebirthAI/hyperflow-h3-flash` (ref2va_int8_convrot_comfyui)
* **Mode:** **Interactive Human Web UI**
* **Accelerator:** Kaggle Dual Nvidia Tesla T4 GPU (or P100)
* **Interface:** Full ComfyUI visual graph editor exposed via Cloudflare public tunnel

---

## 🚀 How to Run

### Option 1: Via Kaggle Web Editor (One-Click)
1. Download or open `notebook.ipynb` using the badge in the root README.
2. Create a new notebook on [Kaggle](https://www.kaggle.com/code) and upload `notebook.ipynb`.
3. In **Settings**, set **Accelerator: GPU T4 x2** and **Internet: On**.
4. Run all cells. Cell 4 will print a public Cloudflare link (`https://....trycloudflare.com`).
5. Click the link to open ComfyUI in your browser and create videos interactively!

### Option 2: Via Local Push Dispatcher
```bash
python tools/push_kernel.py workflows/hyperflow-h3-flash --profile my_profile -d my_username/minimax-h3-open-weights
```
*(The server will stay online so you can connect to the public tunnel until you choose to stop it).*
