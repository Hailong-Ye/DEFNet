# DEFNet

Official implementation of **Discrepancy-based Enhancement Fusion Network for RGBT Tracking**.

> Lei Liu, Pengcheng Li, Hailong Ye, Yuhang Wang, and Yun Xiao
> IEEE Sensors Journal

DEFNet treats the discrepancy between the RGB and thermal infrared (TIR) modalities as the residual information that is not sufficiently represented by their shared cross-modal response, and exploits it at both the attention and feature levels.

- **ADEF (Attention Discrepancy-based Enhancement Fusion)** builds modality-specific residual attention by subtracting the shared cross-modal attention response, `Attn'_r = Attn_r - Attn_r * Attn_t` (and symmetrically for TIR), then aggregates the residual attention with each modality's own value features.
- **FDEF (Feature Discrepancy-based Enhancement Fusion)** removes the cross-modal correlated feature response, `V_r - Softmax(Q_t K_r^T / sqrt(d_k)) V_r`, re-weights the residual with the scaled cross-modal correlation, and integrates both directions with query-based residual connections and an MLP.

ADEF is inserted after transformer blocks 4, 7 and 10 (`TBSI_LOC: [3, 6, 9]`, zero-based), and FDEF is applied after the last transformer block.

## Results

| Dataset | PR | NPR | SR |
|---|---|---|---|
| GTOT | 92.4 | - | 77.0 |
| RGBT210 | 87.9 | - | 64.8 |
| RGBT234 | 89.1 | - | 67.0 |
| LasHeR | 71.9 | 68.0 | 57.2 |

## Environment

Tested with Python 3.8, PyTorch 1.9.0 and CUDA 10.2 (training on 2 x RTX 3080 Ti).

```bash
conda create -n defnet python=3.8
conda activate defnet
bash install.sh
# or: pip install -r requirements.txt
```

## Data preparation

Datasets are expected under `data/` (edit `_DATA_DIR` in `lib/test/evaluation/local.py` and `data_dir` in `lib/train/admin/local.py` if they live elsewhere). The paths below must point to directories whose direct children are the sequence folders:

```
DEFNet/
  data/
    LasHeR/
      trainingset/<sequence>/{init.txt, visible/, infrared/}
      testingset/<sequence>/{init.txt, visible/, infrared/}
    RGBT210/<sequence>/{init.txt, visible/, infrared/}
    RGBT234/<sequence>/{init.txt, visible/, infrared/}
    GTOT/<sequence>/{init.txt, v/, i/}
```

- LasHeR: https://github.com/BUGPLEASEOUT/LasHeR
- RGBT210 / RGBT234 / GTOT: https://github.com/mmic-lcl/Datasets-and-benchmark-code

## Pretrained model

Training is initialized from the OSTrack ViT-B/16 SOT checkpoint `OSTrack_ep0300.pth.tar`, which should be placed under `pretrained_models/`:

```
DEFNet/pretrained_models/OSTrack_ep0300.pth.tar
```

The checkpoint is available from the [OSTrack](https://github.com/botaoye/OSTrack) repository.

## Training

```bash
python tracking/train.py --script tbsi_track \
  --config vitb_256_tbsi_32x1_1e4_lasher_15ep_sot \
  --save_dir ./output --mode single
```

Use `--mode multiple --nproc_per_node 2` for multi-GPU training.

## Evaluation

```bash
python tracking/test.py --tracker_name tbsi_track \
  --tracker_param vitb_256_tbsi_32x1_1e4_lasher_15ep_sot \
  --runid 10 --dataset_name lasher --threads 8 --vis_gpus 0

python tracking/analysis_results.py --tracker_name tbsi_track \
  --tracker_param vitb_256_tbsi_32x1_1e4_lasher_15ep_sot \
  --dataset_name lasher --runid 10
```

`--dataset_name` can be `lasher`, `rgbt210`, `rgbt234` or `gtot`.

## Code structure

```
lib/models/tbsi_track/vit_tbsi_care.py   # shared ViT backbone; ADEF (Fusion_Layers) and FDEF (Final_Fusion)
lib/models/layers/qkv_newer.py           # ADEF: Difference_Module1 / Fun1
                                         # FDEF: Difference_Module / Fun / Fusion
experiments/tbsi_track/vitb_256_tbsi_32x1_1e4_lasher_15ep_sot.yaml
```

## Citation

```bibtex
@article{liu2026defnet,
  title   = {Discrepancy-based Enhancement Fusion Network for RGBT Tracking},
  author  = {Liu, Lei and Li, Pengcheng and Ye, Hailong and Wang, Yuhang and Xiao, Yun},
  journal = {IEEE Sensors Journal},
  year    = {2026}
}
```

## Acknowledgments

This code is developed upon [OSTrack](https://github.com/botaoye/OSTrack) and [TBSI](https://github.com/RyanHTR/TBSI). We thank the authors for their excellent work.

## License

MIT License, see [LICENSE](LICENSE).
