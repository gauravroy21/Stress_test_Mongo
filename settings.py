import os

DEFAULTS = {'DB_NAME': 'sample',
            'COLLECTION_NAME': 'stress_documents',
            #'CLUSTER_URL': f'mongodb://your_username:your_password@128.105.145.253:27017/test',
            #mongodb://your_username:your_password@128.105.145.253:27017/your_database_name
            #Working Wisconsin Cluster
            'CLUSTER_URL': f'mongodb://128.105.145.80:27017/test',
            #Clemson Cluster
            #'CLUSTER_URL': f'mongodb://130.127.133.98:27017/test',
            'DOCS_PER_BATCH': 100,
            'INSERT_WEIGHT': 1,
            'FIND_WEIGHT': 3,
            'BULK_INSERT_WEIGHT': 1,
            'AGG_PIPE_WEIGHT': 1}


def init_defaults_from_env():
    for key in DEFAULTS.keys():
        value = os.environ.get(key)
        if value:
            DEFAULTS[key] = value


# get the settings from the environment variables
init_defaults_from_env()
