# 🎬 MiniMax Face Refine (VoSR2 Super-Resolution) (Interactive Human Mode)

Method 3: VoSR2 Video Super-Resolution: Feed-forward video super-resolution pass providing 16x micro-texture detail and sharpness on low-resolution faces.

---

## 🎨 Included Workflows (`workflows/`)
* [**`WF3_VOSR2_SuperRes_UI.json`**](workflows/WF3_VOSR2_SuperRes_UI.json) — ComfyUI Visual Graph Editor Workflow
* [**`WF3_VOSR2_SuperRes_API.json`**](workflows/WF3_VOSR2_SuperRes_API.json) — REST API Format Workflow

## 🚀 How to Run
```bash
python tools/push_kernel.py runners/minimax-face-refine-vosr2 --profile my_profile -d my_username/minimax-h3-open-weights
```
