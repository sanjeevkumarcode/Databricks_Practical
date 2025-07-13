# Databricks notebook source
dbutils.fs.help()

# COMMAND ----------

dbutils.notebook.help()

# COMMAND ----------

dbutils.notebook.help('exit')

# COMMAND ----------

firstname = 'sanjeev'
dbutils.notebook.exit(firstname)

# COMMAND ----------

lastname = 'kumar'
print(lastname)

# COMMAND ----------

dbutils.notebook.help()

# COMMAND ----------

ac = 'sanjeev'
dbutils.notebook.exit(ac)


# COMMAND ----------

dbutils.notebook.help('run')

# COMMAND ----------

dbutils.notebook.run('/Workspace/Users/sanjeevanupam80@gmail.com/7. DBUTILS.FS_PRACTICAL', 10)