# igapa2
Igapa with multi source data pull - Jira or from DB.

# Usage
## Automation - using the config files to drive connectivity.

**_config.py** - holds the DB connection string parameters (db, port, user, pw, schema).

**config_admin.ini** - Among other things, holds the JIRA credentials if you are extracting CSV from JIRA ticket.

### Execution example:
_pull data from database and visualize_ > python igapa.py

_pull data from JIRA using ticket EXA-28727_ > python igapa.py 28727

# Subroutines and Tools
**_config.py** - Database connectivity parameters such as credentials.

**config_admin.ini** - JIRA credentials, logging level and visualization properties.

**config_reports.ini** - Visualization properties, which tables and columns to visualize.

**config_report2.ini** - Alternative visualization properties, which tables and columns to visualize.

**export_cloud_to_csv.py** - Creates directory of server_name (from *_config.py*) and extracts a single database table to local csv using same name.

**export_JIRA_to-csv.py** - Passed EXA- ticket and calls *subr_jira_download.py*.

**subr_jira_download.py** - Passed EXA- ticket and downloads EXA- ticket attached files.

**igapa_master** - Main program. This is what is execute in Python.

**subr_char_4_rows.py** - Reads config file and builds charts.

**subr_validate_ticket.py** - Validate JIRA ticket exists on system.

**test_get_config_tbls.py** - Reads config file, extracts Tables and calls *export_cloud_to_csv.py*.

**tools_get_table_cols.py** - Pass in table, get back table columns

**tools_logger.py** - Set up logging. Imported by programs using logging.

