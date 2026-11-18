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

| Workflow / Runner | Description | Links (Interactive & Headless) | Data Sources & Fallback Order |
| :--- | :--- | :--- | :--- |
| **HyperFlow H3 Flash Ref2VA INT8** | Joint video & 32 kHz stereo audio reference generation via MiniMax H3 Flash LoRA. Dual T4 GPU. Pre-loads [ComfyUI Workflows](runners/hyperflow-h3-flash/workflows/). | **Interactive UI:** [<img src="images/download-for-kaggle.svg" width="110" height="34" alt="Kaggle UI"/>](runners/hyperflow-h3-flash/notebook.ipynb) [<img src="images/open-in-colab.svg" width="110" height="34" alt="Colab UI"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/runners/hyperflow-h3-flash/notebook.ipynb)<br>**Headless Batch:** [<img src="images/download-for-kaggle.svg" width="110" height="34" alt="Kaggle Batch"/>](runners/hyperflow-h3-flash_headless_mode/notebook.ipynb) [<img src="images/open-in-colab.svg" width="110" height="34" alt="Colab Batch"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/runners/hyperflow-h3-flash_headless_mode/notebook.ipynb) | **1. Primary (0s Mount):** Kaggle Dataset (`*minimax*weights*`)<br>**2. Fallback (Auto-Download):** Hugging Face (`VideoRebirthAI` & `Comfy-Org`) |
| **Qwen3-TTS 1.7B Voice Studio** | Advanced voice cloning, natural language voice design, and -14 LUFS broadcast mastering. Fast inference on Single T4 / P100. | **Interactive UI:** [<img src="images/download-for-kaggle.svg" width="110" height="34" alt="Kaggle UI"/>](runners/qwen3-tts-studio/notebook.ipynb) [<img src="images/open-in-colab.svg" width="110" height="34" alt="Colab UI"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/runners/qwen3-tts-studio/notebook.ipynb)<br>**Headless Batch:** [<img src="images/download-for-kaggle.svg" width="110" height="34" alt="Kaggle Batch"/>](runners/qwen3-tts-studio_headless_mode/notebook.ipynb) [<img src="images/open-in-colab.svg" width="110" height="34" alt="Colab Batch"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/runners/qwen3-tts-studio_headless_mode/notebook.ipynb) | **Direct (High-Speed):** Hugging Face (`Qwen/Qwen3-TTS-12Hz-1.7B-Base` & `VoiceDesign`) |
| **Face Refine: Gaussian Feathering (Method 1)** | Method 1: Seamless natural edge blending and soft skin feathering for wide shots with zero hard mask borders. Pre-loads WF1 into ComfyUI. Dual T4. | **Interactive UI:** [<img src="images/download-for-kaggle.svg" width="110" height="34" alt="Kaggle UI"/>](runners/minimax-face-refine-gaussian/notebook.ipynb) [<img src="images/open-in-colab.svg" width="110" height="34" alt="Colab UI"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/runners/minimax-face-refine-gaussian/notebook.ipynb)<br>**Headless Batch:** [<img src="images/download-for-kaggle.svg" width="110" height="34" alt="Kaggle Batch"/>](runners/minimax-face-refine-gaussian_headless_mode/notebook.ipynb) [<img src="images/open-in-colab.svg" width="110" height="34" alt="Colab Batch"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/runners/minimax-face-refine-gaussian_headless_mode/notebook.ipynb) | **1. Primary (0s Mount):** Kaggle Dataset (`*minimax*weights*`)<br>**2. Fallback:** Hugging Face (`Comfy-Org/MiniMax-H3`) |
| **Face Refine: SAM Jawline Contour (Method 2)** | Method 2: Segment-Anything semantic contour segmentation to lock jawlines, collars, sunglasses, and props without color bleeding. Pre-loads WF2. Dual T4. | **Interactive UI:** [<img src="images/download-for-kaggle.svg" width="110" height="34" alt="Kaggle UI"/>](runners/minimax-face-refine-sam/notebook.ipynb) [<img src="images/open-in-colab.svg" width="110" height="34" alt="Colab UI"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/runners/minimax-face-refine-sam/notebook.ipynb)<br>**Headless Batch:** [<img src="images/download-for-kaggle.svg" width="110" height="34" alt="Kaggle Batch"/>](runners/minimax-face-refine-sam_headless_mode/notebook.ipynb) [<img src="images/open-in-colab.svg" width="110" height="34" alt="Colab Batch"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/runners/minimax-face-refine-sam_headless_mode/notebook.ipynb) | **1. Primary (0s Mount):** Kaggle Dataset (`*minimax*weights*`)<br>**2. Fallback:** Meta SAM (`sam_vit_b`) & Hugging Face |
| **Face Refine: VoSR2 Super-Resolution (Method 3)** | Method 3: Feed-forward video super-resolution pass providing 16x micro-texture detail and sharpness on low-resolution faces. Pre-loads WF3. Dual T4. | **Interactive UI:** [<img src="images/download-for-kaggle.svg" width="110" height="34" alt="Kaggle UI"/>](runners/minimax-face-refine-vosr2/notebook.ipynb) [<img src="images/open-in-colab.svg" width="110" height="34" alt="Colab UI"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/runners/minimax-face-refine-vosr2/notebook.ipynb)<br>**Headless Batch:** [<img src="images/download-for-kaggle.svg" width="110" height="34" alt="Kaggle Batch"/>](runners/minimax-face-refine-vosr2_headless_mode/notebook.ipynb) [<img src="images/open-in-colab.svg" width="110" height="34" alt="Colab Batch"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/runners/minimax-face-refine-vosr2_headless_mode/notebook.ipynb) | **1. Primary (0s Mount):** Kaggle Dataset (`*minimax*weights*`)<br>**2. Fallback:** Hugging Face (`fearnworks/vosr2`) |
| **Tencent MimicMotion** | Pose-guided human motion video transfer from a reference portrait image and driving pose video using confidence-aware latent fusion. Dual T4. | **Interactive UI:** [<img src="images/download-for-kaggle.svg" width="110" height="34" alt="Kaggle UI"/>](runners/tencent-mimicmotion/notebook.ipynb) [<img src="images/open-in-colab.svg" width="110" height="34" alt="Colab UI"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/runners/tencent-mimicmotion/notebook.ipynb)<br>**Headless Batch:** [<img src="images/download-for-kaggle.svg" width="110" height="34" alt="Kaggle Batch"/>](runners/tencent-mimicmotion_headless_mode/notebook.ipynb) [<img src="images/open-in-colab.svg" width="110" height="34" alt="Colab Batch"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/runners/tencent-mimicmotion_headless_mode/notebook.ipynb) | **Direct (High-Speed):** Hugging Face (`Tencent/MimicMotion` & SVD-XT) |
| **Viggle Remake (Wan2GP)** | Video-to-video recast/swap/edit re-rendering using Wan2GP MiniMax H3 20B INT8 tensor-parallel DiT on Dual T4 GPUs. | **Interactive UI:** [<img src="images/download-for-kaggle.svg" width="110" height="34" alt="Kaggle UI"/>](runners/viggle-remake/notebook.ipynb) [<img src="images/open-in-colab.svg" width="110" height="34" alt="Colab UI"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/runners/viggle-remake/notebook.ipynb)<br>**Headless Batch:** [<img src="images/download-for-kaggle.svg" width="110" height="34" alt="Kaggle Batch"/>](runners/viggle-remake_headless_mode/notebook.ipynb) [<img src="images/open-in-colab.svg" width="110" height="34" alt="Colab Batch"/>](https://colab.research.google.com/github/reactnative1/kaggle-notebooks/blob/main/runners/viggle-remake_headless_mode/notebook.ipynb) | **Direct (High-Speed):** Hugging Face (`Viggle/Viggle-Remake` & `DeepBeepMeep/MiniMax-H3`) |

---

## 🎨 Included ComfyUI Workflow Files (`.json`)

All actual visual graph workflows are committed directly in the repository:

* [**`hyperflow_ref2v_int8.json`**](runners/hyperflow-h3-flash/workflows/hyperflow_ref2v_int8.json) — HyperFlow Reference-to-Video & Audio
* [**`hyperflow_i2v_int8.json`**](runners/hyperflow-h3-flash/workflows/hyperflow_i2v_int8.json) — HyperFlow Image-to-Video & Audio
* [**`hyperflow_t2v_int8.json`**](runners/hyperflow-h3-flash/workflows/hyperflow_t2v_int8.json) — HyperFlow Text-to-Video & Audio
* [**`hyperflow_flf2v_int8.json`**](runners/hyperflow-h3-flash/workflows/hyperflow_flf2v_int8.json) — HyperFlow First-to-Last Frame Interpolation
* [**`WF1_Gaussian_UI.json`**](runners/minimax-face-refine-gaussian/workflows/WF1_Gaussian_UI.json) & [**`WF1_Gaussian_API.json`**](runners/minimax-face-refine-gaussian/workflows/WF1_Gaussian_API.json) — Face Refine Method 1 (Gaussian Feathering)
* [**`WF2_SAM_Contour_UI.json`**](runners/minimax-face-refine-sam/workflows/WF2_SAM_Contour_UI.json) & [**`WF2_SAM_Contour_API.json`**](runners/minimax-face-refine-sam/workflows/WF2_SAM_Contour_API.json) — Face Refine Method 2 (SAM Semantic Jawline)
* [**`WF3_VOSR2_SuperRes_UI.json`**](runners/minimax-face-refine-vosr2/workflows/WF3_VOSR2_SuperRes_UI.json) & [**`WF3_VOSR2_SuperRes_API.json`**](runners/minimax-face-refine-vosr2/workflows/WF3_VOSR2_SuperRes_API.json) — Face Refine Method 3 (VoSR2 Super-Resolution)

---

## 🛠️ Local Push Dispatcher (Zero Account Exposure)

Push any runner directly to Kaggle using your local profile without touching Git:

```bash
# Push Interactive Human UI
python tools/push_kernel.py runners/<runner_name>

# Push Autonomous Headless Batch Runner
python tools/push_kernel.py runners/<runner_name>_headless_mode

# Optional: attach profile or public weights dataset
python tools/push_kernel.py runners/<runner_name> --profile my_account -d my_username/minimax-h3-open-weights
```
