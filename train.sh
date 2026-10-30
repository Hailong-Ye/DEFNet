#!/usr/bin/env bash
# Single-GPU training on LasHeR (about 10 epochs).
python tracking/train.py --script tbsi_track \
  --config vitb_256_tbsi_32x1_1e4_lasher_15ep_sot \
  --save_dir ./output --mode single

# Multi-GPU alternative:
# python tracking/train.py --script tbsi_track \
#   --config vitb_256_tbsi_32x1_1e4_lasher_15ep_sot \
#   --save_dir ./output --mode multiple --nproc_per_node 2
