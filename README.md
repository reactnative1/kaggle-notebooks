# AI Kaggle Cloud Notebooks

Welcome to my collection of Kaggle and Google Colab notebooks for generative AI workflows. This repository hosts free, easy-to-use cloud GPU runners that you can run directly in your browser or cloud environment.

> [!IMPORTANT]
> **How to run a Kaggle notebook:**
> 1. Click **Download for Kaggle**, then click the **Download raw file** button at the top right of the file page.
> 2. Sign in at [kaggle.com](https://www.kaggle.com), go to **Code**, and click **New Notebook**.
> 3. In the notebook editor, open **File → Import Notebook** (or **Upload Notebook**) and upload the `.ipynb` file you downloaded.
> 4. In the right panel, set **Session options → Accelerator → GPU T4 x2** (or **P100**) and turn **Internet** on.
> 5. Run the cells from top to bottom.

---

## Notebooks

| Notebook Name | Description | Data Sources & Fallback Order | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Links&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| :--- | :--- | :--- | :---: |
| **HyperFlow H3 Flash Ref2VA INT8 (Interactive UI)** | Human Interactive Mode: Boots ComfyUI visual web editor exposed via a public Cloudflare tunnel. Experiment, upload custom references, and generate videos with live preview in your browser. Optimized for Kaggle GPU T4 x2. | **1. Primary (0-Sec Mount):**<br>• Kaggle Dataset (`/kaggle/input/*minimax*weights*`)<br><br>**2. Fallback (Auto-Download):**<br>• Hugging Face (`VideoRebirthAI/hyperflow-h3-flash`)<br>• Hugging Face (`Comfy-Org/MiniMax-H3`) | [<img src="images/download-for-kaggle.svg" width="133" height="42" alt="Download for Kaggle"/>](workflows/hyperflow-h3-flash/notebook.ipynb)<br>[<img src="images/open-in-colab.svg" width="133" height="42" alt="Open in Colab"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/workflows/hyperflow-h3-flash/notebook.ipynb) |
| **HyperFlow H3 Flash Ref2VA INT8 (Headless Batch)** | Autonomous Agent Mode: Headless batch runner for AI agents (Antigravity). Executes multi-shot queues with per-job fault tolerance, streams outputs immediately, and auto-terminates upon completion to preserve GPU quota. Optimized for Kaggle GPU T4 x2. | **1. Primary (0-Sec Mount):**<br>• Kaggle Dataset (`/kaggle/input/*minimax*weights*`)<br><br>**2. Fallback (Auto-Download):**<br>• Hugging Face (`VideoRebirthAI/hyperflow-h3-flash`)<br>• Hugging Face (`Comfy-Org/MiniMax-H3`) | [<img src="images/download-for-kaggle.svg" width="133" height="42" alt="Download for Kaggle"/>](workflows/hyperflow-h3-flash_headless_mode/notebook.ipynb)<br>[<img src="images/open-in-colab.svg" width="133" height="42" alt="Open in Colab"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/workflows/hyperflow-h3-flash_headless_mode/notebook.ipynb) |

---

## 🚀 Local Push Dispatcher (Zero Account Exposure)

For developers who use the Kaggle CLI and want to push directly from their terminal without manually uploading:

```bash
# Push Interactive Human UI
python tools/push_kernel.py workflows/hyperflow-h3-flash

# Push Autonomous Headless Batch Runner
python tools/push_kernel.py workflows/hyperflow-h3-flash_headless_mode

# Optional: attach profile or public weights dataset
python tools/push_kernel.py workflows/hyperflow-h3-flash_headless_mode --profile my_account -d my_username/minimax-h3-open-weights
```
*(The dispatcher automatically reads your local profile, creates a temporary metadata file, pushes, and removes it so zero personal account info is committed to Git).*
