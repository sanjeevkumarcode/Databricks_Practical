# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMP VIEW salesdata AS SELECT * FROM csv.`dbfs:/Output/CSV_1207.csv`

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesdata;

# COMMAND ----------

# MAGIC %sql
# MAGIC select avg(try_cast(_c2 as int)) as avg_population from salesdata;