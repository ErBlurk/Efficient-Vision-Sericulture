# 3. Models

#### Segmentation results comparison:

| Method | Pixel Acc. (↑) | IoU (background ↑) | IoU (worms ↑) | IoU (leaves ↑) | mIoU (↑) |
| --- | --- | --- | --- | --- | --- |
| U-Net | 0.1524 | 0.0296 | 0.0599 | 0.1239 | 0.0712 |
| SegFormer-B0 | 0.1842 | 0.1051 | 0.0541 | 0.1383 | 0.0992 |
| Heuristics | **0.6453** | **0.3756** | **0.3668** | **0.6168** | **0.4531** |

---

#### Classification results comparison:

| Pipeline | Model | Accuracy (↑) | Precision (↑) | Recall (↑) | F1 (↑) | Specificity (↑) | FPR (↓) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DDP | EfficientNetV2 | **0.9556** | 0.9408 | **0.9795** | **0.9597** | 0.9274 | 0.0726 |
|  | RepNeXt | 0.9481 | 0.9342 | 0.9726 | 0.9530 | 0.9194 | 0.0806 |
|  | MobileViT | 0.9037 | **0.9839** | 0.8356 | 0.9037 | **0.9839** | **0.0161** |
| EPP | Threshold | 0.9410 | **0.9304** | 0.9671 | 0.9484 | **0.9076** | **0.0924** |
|  | Log. Reg. | **0.9483** | 0.9207 | **0.9934** | **0.9557** | 0.8908 | 0.1092 |

---

#### Classification pipelines efficiency comparison:

| Pipeline | Model          | Params (M ↓) | Size (MB ↓) | GFLOPs (↓) | FPS (img/s ↑) | Latency (ms ↓) |
| :------- | :------------- | :----------- | :---------- | :--------- | :------------ | :------------- |
| DDP      | EfficientNetV2 | 20.18        | 77.83       | 184.98     | 11.10         | 89.80 ± 0.13   |
|          | RepNeXt        | 4.55         | 18.02       | 56.64      | 17.87         | 55.94 ± 0.20   |
|          | MobileViT      | 4.94         | 19.01       | 91.30      | 5.78          | 173.03 ± 55.80 |
| EPP      | Threshold      | -            | < 0.01      | ∼ 1.79     | 61.70         | 19.22 ± 0.34   |
|          | Log. Reg.      | < 103        | < 0.01      | ∼ 1.79     | 61.70         | 19.22 ± 0.34   |

---

#### Segmentation accuracy on gold standard:

| Method       | Pixel Acc. (↑) | IoU (background ↑) | IoU (worms ↑) | IoU (leaves ↑) | mIoU (↑) |
| :----------- | :------------- | :----------------- | :------------ | :------------- | :------- |
| U-Net        | 0.1524         | 0.0296             | 0.0599        | 0.1239         | 0.0712   |
| SegFormer-B0 | 0.1842         | 0.1051             | 0.0541        | 0.1383         | 0.0992   |
| Heuristics   | 0.6453         | 0.3756             | 0.3668        | 0.6168         | 0.4531   |