
# Superset configuration file

# The Superset server base URL
SUPERSET_WEBSERVER_BASEURL = 'http://localhost:8080'

# The database connection details
DATABASES = {
    'default': {
        'ENGINE': 'mysql',
        'NAME': 'CI_CD',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': 3306
    }
}

# The SQLAlchemy connection string
SQLALCHEMY_DATABASE_URI = 'mysql -h 127.0.0.1 -P 3306 -u root'

# The Superset secret key
SECRET_KEY = 'EAUNItmUZddw5GkDraygRtLPtxiHX94o+75C28cTmFc='

# The default theme
DEFAULT_THEME = 'superset-dark'

# The number of results to display per page
ROWS_PER_PAGE = 10

# The number of columns to show in the exploration results table
EXPLORATION_RESULTS_TABLE_COLUMNS = 5

# The maximum number of rows to show in a dataset table
DATASET_TABLE_MAX_ROWS = 1000

# The maximum number of records to fetch from a database in a single query
MAX_ROW_FETCH = 100000

# The cache configuration
CACHE_CONFIG = {
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': '/tmp/superset-cache'
}


# The Flask-SQLAlchemy connection pool size
SQLALCHEMY_POOL_SIZE = 5

# Custom configuration
CUSTOM_CONFIG = {
    'data_dir': '/app/superset/data/',
}
