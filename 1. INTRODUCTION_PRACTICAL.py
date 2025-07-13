# Databricks notebook source
display(dbutils.fs.ls('/'))

# COMMAND ----------

display(dbutils.fs.ls('dbfs:/FileStore/'))

# COMMAND ----------

display(dbutils.fs.ls('dbfs:/FileStore/Excel_Practise.xlsx/'))

# COMMAND ----------

display(dbutils.fs.ls('dbfs:/FileStore/CSV_1207.csv/'))

# COMMAND ----------

df = spark.read.option('header',True).csv('dbfs:/FileStore/CSV_1207.csv/')

# COMMAND ----------

df.show()

# COMMAND ----------

df.display()

# COMMAND ----------

dbutils.fs.help()