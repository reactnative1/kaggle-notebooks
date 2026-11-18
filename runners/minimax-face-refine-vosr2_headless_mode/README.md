# 🤖 MiniMax Face Refine (VoSR2 Super-Resolution) (Headless Mode)

Autonomous batch face restoration pipeline for AI agents (Method 3: VoSR2 Video Super-Resolution).

---

## 🛡️ Features
1. Multi-clip queue defined in `BATCH_CLIPS` (Cell 1).
2. Per-clip fault tolerance (`try...except`).
3. Immediate file streaming to `/kaggle/working/outputs/`.
4. Auto-termination on completion (`sys.exit(0)`).

## 🚀 How to Run
```bash
python tools/push_kernel.py runners/minimax-face-refine-vosr2_headless_mode --profile my_profile -d my_username/minimax-h3-open-weights
```
