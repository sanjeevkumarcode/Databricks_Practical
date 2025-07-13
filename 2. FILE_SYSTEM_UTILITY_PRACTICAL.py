# Databricks notebook source
dbutils.fs.help()

# COMMAND ----------

dbutils.fs.cp('dbfs:/FileStore/CSV_1207.csv','dbfs:/Output/CSV_1207.csv')

# COMMAND ----------

ab = dbutils.fs.ls('dbfs:/Output/CSV_1207.csv')
display(ab)

# COMMAND ----------

aa = spark.read.option('header',True).csv('dbfs:/Output/CSV_1207.csv/')
display(aa)

# COMMAND ----------

dbutils.fs.cp('dbfs:/Output/','dbfs:/Input/', True)

# COMMAND ----------

dbutils.fs.cp('dbfs:/FileStore/','dbfs:/Output/',True)

# COMMAND ----------

display(dbutils.fs.ls('/'))

# COMMAND ----------

dbutils.fs.mkdirs('/Temp/Input')

# COMMAND ----------

df1 = spark.read.option('header',True).csv('dbfs:/Temp2/CSV_1207.csv')
display(df1)

# COMMAND ----------

dbutils.fs.put('dbfs:/Temp2/CSV_1207.csv','1,Sanjeev,23,123', overwrite=True)

# COMMAND ----------

df2 = spark.read.option('header',True).csv('dbfs:/Temp2/CSV_1207.csv')
display(df2)

# COMMAND ----------

dbutils.fs.rm('/Temp', recurse=True)

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

a=dbutils.fs.ls('/')
display(a)

# COMMAND ----------

display(dbutils.fs.ls('dbfs:/Input'))

# COMMAND ----------

ab = spark.read.option('header',True).csv('dbfs:/Input/CSV_1207.csv')
display(ab)

# COMMAND ----------

dbutils.fs.mkdirs('/Directory')

# COMMAND ----------

dbutils.fs.cp('dbfs:/Input/CSV_1207.csv','dbfs:/Directory/',True)

# COMMAND ----------

dbutils.fs.mv('dbfs:/Output/Excel_Practise.xlsx','dbfs:/Directory/',True)

# COMMAND ----------

dbutils.fs.rm('dbfs:/Temp2',True)

# COMMAND ----------

dbutils.fs.put('dbfs:/Temp2/Excel_Practise/xlsx', '12', True)

# COMMAND ----------

ac= spark.read.option('header',True).csv('dbfs:/Input/CSV_1207.csv')
display(ac)

# COMMAND ----------

ad  = spark.read.option('header',True).csv('dbfs:/Input/CSV_1207.csv')
display(ad)

# COMMAND ----------

dbutils.fs.head('dbfs:/Input/CSV_1207.csv')