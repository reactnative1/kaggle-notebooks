# 🎬 MiniMax Face Refine (SAM Jawline Contour) (Interactive Human Mode)

Method 2: SAM Semantic Jawline Segmentation: Segment-Anything semantic contour segmentation to isolate jawlines, collars, sunglasses, and props without color bleeding.

---

## 🎨 Included Workflows (`workflows/`)
* [**`WF2_SAM_Contour_UI.json`**](workflows/WF2_SAM_Contour_UI.json) — ComfyUI Visual Graph Editor Workflow
* [**`WF2_SAM_Contour_API.json`**](workflows/WF2_SAM_Contour_API.json) — REST API Format Workflow

## 🚀 How to Run
```bash
python tools/push_kernel.py runners/minimax-face-refine-sam --profile my_profile -d my_username/minimax-h3-open-weights
```
