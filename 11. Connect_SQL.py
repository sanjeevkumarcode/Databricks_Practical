# Databricks notebook source
driver = "com.microsoft.sqlserver.jdbc.SQLServerDriver"

database_host = "azuresqldb-test27062025.database.windows.net"
database_port = "1433" # update if you use a non-default port
database_name = "testdb"
table = "Customer"
user = "sanjeev"
password = "DHIWARbarh7#"

url = f"jdbc:sqlserver://{database_host}:{database_port}/{database_name}"

# COMMAND ----------

remote_table = (spark.read
  .format("jdbc")
  .option("driver", driver)
  .option("url", url)
  .option("dbtable", table)
  .option("user", user)
  .option("password", password)
  .load()
)



# COMMAND ----------

remote_table = "jdbc:sqlserver://<server_name>:1433;databaseName=testdb;user=sanjeev;password=DHIWARbarh7#"
