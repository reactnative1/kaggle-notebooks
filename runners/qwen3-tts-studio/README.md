# 🎙️ Qwen3-TTS 1.7B Studio (Interactive Human Mode)

Interactive, browser-based voice studio for high-fidelity voice cloning, custom voice design, and emotional/paced speech synthesis using **Qwen3-TTS 1.7B** on Kaggle GPU T4.

---

## ⚡ Specifications

* **Models:** `Qwen/Qwen3-TTS-12Hz-1.7B-Base` & `Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign`
* **Mode:** **Interactive Gradio Web UI**
* **Accelerator:** Kaggle Single or Dual Nvidia Tesla T4 GPU (or P100)
* **Mastering:** Automated broadcast loudness normalization (`-14 LUFS`)

---

## 🚀 How to Run

### Option 1: Via Kaggle Web Editor (One-Click)
1. Download or open `notebook.ipynb` using the badge in the root README.
2. Create a new notebook on [Kaggle](https://www.kaggle.com/code) and upload `notebook.ipynb`.
3. In **Settings**, set **Accelerator: GPU T4 x1** (or **P100**) and **Internet: On**.
4. Run all cells. Cell 3 will print a public Cloudflare link (`https://....trycloudflare.com`).
5. Open the link to start synthesizing speech interactively in your browser!

### Option 2: Via Local Push Dispatcher
```bash
python tools/push_kernel.py runners/qwen3-tts-studio --profile my_profile
```
