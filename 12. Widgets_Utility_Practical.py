# Databricks notebook source
dbutils.widgets.help()

# COMMAND ----------

dbutils.widgets.help('Combobox')

# COMMAND ----------

dbutils.widgets.combobox('CountryCB', defaultValue="INDIA", choices = ['INDIA', 'USA', 'UK'], label = "Country_CB")

# COMMAND ----------

dbutils.widgets.help('dropdown')

# COMMAND ----------

dbutils.widgets.dropdown('CountryDD', defaultValue = "INDIA", choices = ['INDIA','USA','UK'], label = "Country_DD")

# COMMAND ----------

dbutils.widgets.help('multiselect')

# COMMAND ----------

dbutils.widgets.multiselect('CountryMS', 'INDIA', ['INDIA','USA','UK'], 'CountryMS')

# COMMAND ----------

dbutils.widgets.help('text')

# COMMAND ----------

dbutils.widgets.text('CountryT', "INDIA")

# COMMAND ----------

dbutils.widgets.help('remove')

# COMMAND ----------

dbutils.widgets.help('removeall')

# COMMAND ----------

dbutils.widgets.help('get')

# COMMAND ----------

dbutils.widgets.get('CountryMS')

# COMMAND ----------

dbutils.widgets.help('getAll')

# COMMAND ----------

dbutils.widgets.get('CountryMS')

# COMMAND ----------

dbutils.widgets.help('getArgument')

# COMMAND ----------

dbutils.widgets.getArgument('CountryMS')