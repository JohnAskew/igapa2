import os

dsn = os.environ.get('EXAHOST', 'demodb.exasol.com')
port = 8563
user = os.environ.get('EXAUID', 'exasol_user')
password = os.environ.get('EXAPWD', 'secret')
schema = os.environ.get('EXASCHEMA', 'EXA_STATISTICS')
