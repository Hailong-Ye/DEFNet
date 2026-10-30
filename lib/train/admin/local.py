import os


class EnvironmentSettings:
    """Local paths used for training. Everything is relative to this repository."""

    def __init__(self):
        # Repository root: <repo>/lib/train/admin/local.py -> <repo>
        repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
        data_dir = os.path.join(repo_dir, 'data')

        self.workspace_dir = repo_dir    # Base directory for saving network checkpoints.
        self.tensorboard_dir = os.path.join(repo_dir, 'tensorboard')    # Directory for tensorboard files.
        self.pretrained_networks = os.path.join(repo_dir, 'pretrained_models')

        # LasHeR: the directory must directly contain the sequence folders
        # (each sequence folder has init.txt, visible/ and infrared/).
        self.lasher_train_dir = os.path.join(data_dir, 'LasHeR', 'trainingset')
        self.lasher_test_dir = os.path.join(data_dir, 'LasHeR', 'testingset')

        # Not used by DEFNet; kept for compatibility with the upstream code.
        self.lasot_dir = ''
        self.got10k_dir = ''
        self.got10k_val_dir = ''
        self.lasot_lmdb_dir = ''
        self.got10k_lmdb_dir = ''
        self.trackingnet_dir = ''
        self.trackingnet_lmdb_dir = ''
        self.coco_dir = ''
        self.coco_lmdb_dir = ''
        self.lvis_dir = ''
        self.sbd_dir = ''
        self.imagenet_dir = ''
        self.imagenet_lmdb_dir = ''
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
        self.davis_dir = ''
        self.youtubevos_dir = ''
