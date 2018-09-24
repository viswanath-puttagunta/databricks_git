# Databricks notebook source
from pyspark.sql import *
from pyspark.sql.functions import lit
from pyspark.sql.functions import max
from pyspark.sql.functions import count
import numpy as np
from pyspark.ml.feature import Imputer

# COMMAND ----------

# MAGIC %md # Hello this is a title

# COMMAND ----------

housingdf = spark.read.format("csv").options(header='true', delimiter = ',').load("/FileStore/tables/iowa_housing_train-a8462.csv")

# COMMAND ----------

display(housingdf)

# COMMAND ----------

df.count()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

