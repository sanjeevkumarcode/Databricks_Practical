# Databricks notebook source
dbutils.help()

# COMMAND ----------

dbutils.data.help()

# COMMAND ----------

dbutils.data.help('summarize')

# COMMAND ----------

data = [(1,'sanjeev'),(2,'asatyam'),(3,'maheer')]
column = ['id','name']
df = spark.createDataFrame(data,column)
display(df)

# COMMAND ----------

dbutils.data.summarize(df)