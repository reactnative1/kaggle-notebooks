# 🎬 HyperFlow H3 Flash Ref2VA Studio (Interactive Human Mode)

Interactive, browser-based cloud runner for joint video & audio reference generation using **MiniMax H3 Flash LoRA** on Kaggle Dual Nvidia Tesla T4 GPUs.

---

## ⚡ Specifications

* **Model:** `VideoRebirthAI/hyperflow-h3-flash` (ref2va_int8_convrot_comfyui)
* **Mode:** **Interactive Human Web UI**
* **Accelerator:** Kaggle Dual Nvidia Tesla T4 GPU (or P100)
* **Interface:** Full ComfyUI visual graph editor exposed via Cloudflare public tunnel

---

## 🎨 Included ComfyUI Workflows (`.json`)

The following official ComfyUI workflows are included directly in this repository under [`workflows/`](workflows/):

| Workflow File | Description | Mode |
| :--- | :--- | :--- |
| [**`hyperflow_ref2v_int8.json`**](workflows/hyperflow_ref2v_int8.json) | Reference-to-Video & Audio | Recast/generate video matching 1 or 2 reference images + text prompt |
| [**`hyperflow_i2v_int8.json`**](workflows/hyperflow_i2v_int8.json) | Image-to-Video & Audio | Animate a single initial frame with synchronized audio |
| [**`hyperflow_t2v_int8.json`**](workflows/hyperflow_t2v_int8.json) | Text-to-Video & Audio | Generate joint video + audio directly from a text prompt |
| [**`hyperflow_flf2v_int8.json`**](workflows/hyperflow_flf2v_int8.json) | First-Last Frame-to-Video | Interpolate video between a start frame and an end frame |

> [!NOTE]
> When you run the notebook, all of these workflows are automatically pre-loaded into ComfyUI's internal `user/default/workflows/` directory so you can select them directly from ComfyUI's **Workflows** dropdown menu, or simply drag and drop the `.json` file onto the canvas!

---

## 🚀 How to Run

### Option 1: Via Kaggle Web Editor (One-Click)
1. Download or open `notebook.ipynb` using the badge in the root README.
2. Create a new notebook on [Kaggle](https://www.kaggle.com/code) and upload `notebook.ipynb`.
3. In **Settings**, set **Accelerator: GPU T4 x2** and **Internet: On**.
4. Run all cells. Cell 4 will print a public Cloudflare link (`https://....trycloudflare.com`).
5. Open the link to start creating videos!

### Option 2: Via Local Push Dispatcher
```bash
python tools/push_kernel.py runners/hyperflow-h3-flash --profile my_profile -d my_username/minimax-h3-open-weights
```
*(The server will stay online so you can connect to the public tunnel until you choose to stop it).*
