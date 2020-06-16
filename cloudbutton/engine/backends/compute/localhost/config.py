import multiprocessing


RUNTIME_NAME_DEFAULT = 'localhost'
RUNTIME_TIMEOUT_DEFAULT = 600  # 10 minutes


def load_config(config_data):
    config_data['cloudbutton']['runtime'] = RUNTIME_NAME_DEFAULT
    config_data['cloudbutton']['runtime_memory'] = None
    if 'runtime_timeout' not in config_data['cloudbutton']:
        config_data['cloudbutton']['runtime_timeout'] = RUNTIME_TIMEOUT_DEFAULT

    if 'storage_backend' not in config_data['cloudbutton']:
        config_data['cloudbutton']['storage_backend'] = 'localhost'

    if 'localhost' not in config_data:
        config_data['localhost'] = {}

    if 'ibm_cos' in config_data and 'private_endpoint' in config_data['ibm_cos']:
        del config_data['ibm_cos']['private_endpoint']

    if 'workers' in config_data['cloudbutton']:
        config_data['localhost']['workers'] = config_data['cloudbutton']['workers']
    else:
        total_cores = multiprocessing.cpu_count()
        config_data['cloudbutton']['workers'] = total_cores
        config_data['localhost']['workers'] = total_cores
