# igapa2
Igapa with multi source data pull - Jira or from DB.



# Subroutines and Tools
**export_cloud_to_csv.py** -Extract a single database table to local csv using same name.

**export_JIRA_to-csv.py** - Passed EXA- ticket and calls **subr_jira_download.py**.

**subr_jira_download.py** - Passed EXA- ticket and downloads EXA- ticket attached files.

**test_get_config_tbls.py** - Reads config file, extracts Tables and calls **export_cloud_to_csv.py**.
