# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "f16dbefd-294c-417f-b27c-c41f65613232",
# META       "default_lakehouse_name": "Silver",
# META       "default_lakehouse_workspace_id": "4d01e414-5733-49f1-b10f-f95f3da9469f",
# META       "known_lakehouses": [
# META         {
# META           "id": "f16dbefd-294c-417f-b27c-c41f65613232"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.sql("SELECT * FROM Silver.clean_breweries LIMIT 1000")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.printSchema()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
