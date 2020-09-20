import os, sys
try:
	from pyexasol import ExaConnection
except:
	os.system('pip install pyexasol')
	from pyexasol import ExaConnection

con = ExaConnection(dsn="192.168.1.158", user='sys', password='exasol')
data = con.export_to_pandas('SELECT * from EXA_DBA_AUDIT_SESSIONS WHERE LOGIN_TIME > (SELECT ADD_SECONDS(CURRENT_TIMESTAMP, -184000))')
print(data)

con.export_to_file('./file.exp', 'EXA_DB_SIZE_HOURLY', export_params = {'with_column_names':True, 'columns':['INTERVAL_START','RAW_OBJECT_SIZE_AVG','RAW_OBJECT_SIZE_MAX','MEM_OBJECT_SIZE_AVG','MEM_OBJECT_SIZE_MAX','RECOMMENDED_DB_RAM_SIZE_AVG','RECOMMENDED_DB_RAM_SIZE_MAX','STORAGE_SIZE_AVG','STORAGE_SIZE_MAX']})