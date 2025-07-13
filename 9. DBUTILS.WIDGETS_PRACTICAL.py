# Databricks notebook source
dbutils.widgets.help('')

# COMMAND ----------

dbutils.widgets.combobox(name='fruitsCB', defaultValue='apple', choices = ['apple','orange','banana'], label = 'Fruits Combobox')

# COMMAND ----------

dbutils.widgets.dropdown(name='fruitsDD', defaultValue='apple', choices = ['apple','orange','banana'], label = 'Fruits Dropdown')

# COMMAND ----------

dbutils.widgets.multiselect(name='fruitsMS', defaultValue='apple', choices = ['apple','orange','banana'], label = 'Fruits Multiselect')

# COMMAND ----------

dbutils.widgets.text(name = 'fruitsTB', defaultValue= 'apple', label = 'Fruits Textbox')

# COMMAND ----------

dbutils.widgets.get('fruitsCB')

# COMMAND ----------

dbutils.widgets.get('fruitsCB')

# COMMAND ----------

dbutils.widgets.getArgument('fruitsCB','error:not avl')

# COMMAND ----------

dbutils.widgets.remove('fruitsMS')

# COMMAND ----------

dbutils.widgets.removeAll()