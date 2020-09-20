import os

dsn = os.environ.get('EXAHOST', 'demodb.exasol.com')
port = 8563
user = os.environ.get('EXAUID', 'exasol_joas')
password = os.environ.get('EXAPWD', 'J0hnsPassw0rdShouldB3Ch4ng3d')
schema = os.environ.get('EXASCHEMA', 'EXA_STATISTICS')
