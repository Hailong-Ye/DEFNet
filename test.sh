#!/usr/bin/env bash
# Testing on the four RGBT benchmarks. The checkpoint epoch is set by --runid (10).
for DATASET in lasher rgbt234 rgbt210 gtot; do
  python tracking/test.py --tracker_name tbsi_track \
    --tracker_param vitb_256_tbsi_32x1_1e4_lasher_15ep_sot \
    --runid 10 --dataset_name ${DATASET} --threads 8 --vis_gpus 0
  python tracking/analysis_results.py --tracker_name tbsi_track \
    --tracker_param vitb_256_tbsi_32x1_1e4_lasher_15ep_sot \
    --dataset_name ${DATASET} --runid 10
done
