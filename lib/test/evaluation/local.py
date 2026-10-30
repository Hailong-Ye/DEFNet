import os

from lib.test.evaluation.environment import EnvSettings

# Repository root: <repo>/lib/test/evaluation/local.py -> <repo>
_REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
_DATA_DIR = os.path.join(_REPO_DIR, 'data')
_OUTPUT_DIR = os.path.join(_REPO_DIR, 'output')


def local_env_settings():
    settings = EnvSettings()

    # Project and result paths
    settings.prj_dir = _REPO_DIR
    settings.save_dir = _OUTPUT_DIR
    settings.results_path = os.path.join(_OUTPUT_DIR, 'test', 'tracking_results')
    settings.result_plot_path = os.path.join(_OUTPUT_DIR, 'test', 'result_plots')
    settings.segmentation_path = os.path.join(_OUTPUT_DIR, 'test', 'segmentation_results')
    settings.network_path = os.path.join(_OUTPUT_DIR, 'test', 'networks')

    # RGBT tracking benchmarks (edit _DATA_DIR above if the datasets are stored elsewhere).
    # Every path below must point to a directory whose direct children are the sequence folders.
    settings.lasher_path = os.path.join(_DATA_DIR, 'LasHeR', 'testingset')
    settings.rgbt210_path = os.path.join(_DATA_DIR, 'RGBT210')
    settings.rgbt234_path = os.path.join(_DATA_DIR, 'RGBT234')
    settings.gtot_path = os.path.join(_DATA_DIR, 'GTOT')
    settings.vtuav_path = os.path.join(_DATA_DIR, 'VTUAV')

    return settings
