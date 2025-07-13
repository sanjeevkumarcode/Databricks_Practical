# Databricks notebook source
dbutils.fs.help()

# COMMAND ----------

dbutils.fs.ls('/')

# COMMAND ----------

display(dbutils.fs.ls('/'))

# COMMAND ----------

display(dbutils.fs.ls('dbfs:/Input/'))

# COMMAND ----------

aa = spark.read.option('header', 'true').csv('dbfs:/Input/CSV_1207.csv')
display(aa)