# 🤖 MiniMax Face Refine (SAM Jawline Contour) (Headless Mode)

Autonomous batch face restoration pipeline for AI agents (Method 2: SAM Semantic Jawline Segmentation).

---

## 🛡️ Features
1. Multi-clip queue defined in `BATCH_CLIPS` (Cell 1).
2. Per-clip fault tolerance (`try...except`).
3. Immediate file streaming to `/kaggle/working/outputs/`.
4. Auto-termination on completion (`sys.exit(0)`).

## 🚀 How to Run
```bash
python tools/push_kernel.py runners/minimax-face-refine-sam_headless_mode --profile my_profile -d my_username/minimax-h3-open-weights
```
