# Databricks notebook source
dbutils.fs.help('mount')

# COMMAND ----------

dbutils.fs.mount(
source='wasbs://inputdatabricks@datalakeadf23062025.blob.core.windows.net/',
mount_point='/mnt/input',
extra_configs={'fs.azure.account.key.datalakeadf23062025.blob.core.windows.net':'4hPfCAmxSJzwj10C7vHcZKMVddbixvbZT+TnLhF9iOhQ8rOSVPAQaNtujMiT2Lc3Y02Hq9EMVrFB+AStySToyg=='})

# COMMAND ----------

dbutils.fs.mount(
source='wasbs://outputdatabricks@datalakeadf23062025.blob.core.windows.net/',
mount_point='/mnt/output',
extra_configs={'fs.azure.sas.output.datalakeadf23062025.blob.core.windows.net':'sv=2024-11-04&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2025-07-12T22:39:02Z&st=2025-07-12T14:39:02Z&spr=https&sig=ERGGJo9E3F8Wy9993BQzAqJQ8GRT03ORBC5iwQnPfsU%3D'})

# COMMAND ----------

def get_dbutils(spark):
    from pyspark.dbutils import DBUtils
    return DBUtils(spark)

dbutils = get_dbutils(spark)

dbutils.fs.mount(
    source='wasbs://outputdatabricks@datalakeadf23062025.blob.core.windows.net/',
    mount_point='/mnt/output',
    extra_configs={'fs.azure.sas.output.datalakeadf23062025.blob.core.windows.net': 'sv=2024-11-04&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2025-07-12T22:39:02Z&st=2025-07-12T14:39:02Z&spr=https&sig=ERGGJo9E3F8Wy9993BQzAqJQ8GRT03ORBC5iwQnPfsU%3D'}
)