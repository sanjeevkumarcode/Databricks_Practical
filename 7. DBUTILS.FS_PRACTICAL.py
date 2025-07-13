# Databricks notebook source
dbutils.fs.help()

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help('cp')

# COMMAND ----------

dbutils.fs.cp('dbfs:/Input/CSV_1207.csv','dbfs:/Temp2/')

# COMMAND ----------

dbutils.fs.help('head')

# COMMAND ----------

dbutils.fs.head('dbfs:/Input/CSV_1207.csv')

# COMMAND ----------

dbutils.fs.head('dbfs:/Input/CSV_1207.csv',41)

# COMMAND ----------

dbutils.fs.help('mkdirs')

# COMMAND ----------

dbutils.fs.mkdirs('dbfs:/Temp3')

# COMMAND ----------

dbutils.fs.help('rm')

# COMMAND ----------

dbutils.fs.rm('dbfs:/Temp3')

# COMMAND ----------

dbutils.fs.help('ls')

# COMMAND ----------

dbutils.fs.ls('dbfs:/')

# COMMAND ----------

dbutils.fs.help('mv')

# COMMAND ----------

dbutils.fs.mv('dbfs:/Temp2/Excel_Practise/xlsx','dbfs:/Input/')

# COMMAND ----------

dbutils.fs.help('put')

# COMMAND ----------

dbutils.fs.head('dbfs:/FileStore/sample_2.txt')

# COMMAND ----------

dbutils.fs.put('dbfs:/FileStore/sample_2.txt','Hello I am Sanjeev Kuamr',True)

# COMMAND ----------

dbutils.fs.head('dbfs:/FileStore/sample_2.txt')

# COMMAND ----------

