# AI Kaggle Cloud Notebooks

Welcome to my collection of Kaggle and Google Colab runners for generative AI workflows. This repository hosts free, easy-to-use cloud GPU runners and ComfyUI workflows that you can run directly in your browser or cloud environment.

> [!IMPORTANT]
> **How to run a Kaggle runner:**
> 1. Click **Download for Kaggle**, then click the **Download raw file** button at the top right of the file page.
> 2. Sign in at [kaggle.com](https://www.kaggle.com), go to **Code**, and click **New Notebook**.
> 3. In the notebook editor, open **File → Import Notebook** (or **Upload Notebook**) and upload the `.ipynb` file you downloaded.
> 4. In the right panel, set **Session options → Accelerator → GPU T4 x2** (or **P100**) and turn **Internet** on.
> 5. Run the cells from top to bottom.

---

## 🚀 Cloud Runners & Notebooks

| Runner Name | Description | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Links&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Data Sources & Fallback Order |
| :--- | :--- | :---: | :--- |
| **HyperFlow H3 Flash Ref2VA INT8 (Interactive UI)** | Human Interactive Mode: Boots ComfyUI visual web editor exposed via a public Cloudflare tunnel. Pre-loads official [ComfyUI Workflows](runners/hyperflow-h3-flash/workflows/) into the menu. Optimized for Kaggle GPU T4 x2. | [<img src="images/download-for-kaggle.svg" width="133" height="42" alt="Download for Kaggle"/>](runners/hyperflow-h3-flash/notebook.ipynb)<br>[<img src="images/open-in-colab.svg" width="133" height="42" alt="Open in Colab"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/runners/hyperflow-h3-flash/notebook.ipynb) | **1. Primary (0s Mount):** Kaggle Dataset (`*minimax*weights*`)<br>**2. Fallback (Auto-Download):** Hugging Face (`VideoRebirthAI` & `Comfy-Org`) |
| **HyperFlow H3 Flash Ref2VA INT8 (Headless Batch)** | Autonomous Agent Mode: Headless batch runner for AI agents (Antigravity). Executes multi-shot queues with per-job fault tolerance, streams outputs immediately, and auto-terminates upon completion to preserve GPU quota. | [<img src="images/download-for-kaggle.svg" width="133" height="42" alt="Download for Kaggle"/>](runners/hyperflow-h3-flash_headless_mode/notebook.ipynb)<br>[<img src="images/open-in-colab.svg" width="133" height="42" alt="Open in Colab"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/runners/hyperflow-h3-flash_headless_mode/notebook.ipynb) | **1. Primary (0s Mount):** Kaggle Dataset (`*minimax*weights*`)<br>**2. Fallback (Auto-Download):** Hugging Face (`VideoRebirthAI` & `Comfy-Org`) |

---

## 🎨 Included ComfyUI Workflow Files (`.json`)

All actual ComfyUI visual graph workflows are committed directly in this repository for one-click download:

* [**`hyperflow_ref2v_int8.json`**](runners/hyperflow-h3-flash/workflows/hyperflow_ref2v_int8.json) — Reference-to-Video & Audio (1 or 2 reference images + prompt)
* [**`hyperflow_i2v_int8.json`**](runners/hyperflow-h3-flash/workflows/hyperflow_i2v_int8.json) — Image-to-Video & Audio (animate a single frame)
* [**`hyperflow_t2v_int8.json`**](runners/hyperflow-h3-flash/workflows/hyperflow_t2v_int8.json) — Text-to-Video & Audio (direct text prompt)
* [**`hyperflow_flf2v_int8.json`**](runners/hyperflow-h3-flash/workflows/hyperflow_flf2v_int8.json) — First-to-Last Frame Interpolation

*(When launching the interactive runner, these workflows are automatically pre-loaded into ComfyUI's **Workflows** dropdown menu).*

---

## 🛠️ Local Push Dispatcher (Zero Account Exposure)

Push any runner directly to Kaggle using your local profile without touching Git:

```bash
# Push Interactive Human UI
python tools/push_kernel.py runners/hyperflow-h3-flash

# Push Autonomous Headless Batch Runner
python tools/push_kernel.py runners/hyperflow-h3-flash_headless_mode

# Optional: attach profile or public weights dataset
python tools/push_kernel.py runners/hyperflow-h3-flash_headless_mode --profile my_account -d my_username/minimax-h3-open-weights
```
