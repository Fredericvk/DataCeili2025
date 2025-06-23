# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "6734907e-9d23-4cb7-9769-7d987e29747c",
# META       "default_lakehouse_name": "Bronze",
# META       "default_lakehouse_workspace_id": "4d01e414-5733-49f1-b10f-f95f3da9469f",
# META       "known_lakehouses": [
# META         {
# META           "id": "6734907e-9d23-4cb7-9769-7d987e29747c"
# META         }
# META       ]
# META     },
# META     "environment": {
# META       "environmentId": "23f378f1-a232-9014-4bbe-36ba40874ac6",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# # BronzeToSilver - Breweries

# MARKDOWN ********************

# The goal of this script is to drop any duplicate breweries in the api_breweries table in the bronze Lakehouse and store in the Silver lakehouse.

# CELL ********************

#Variables
path = "2025/06/08/38ee6654-70a7-40da-98ef-4b7821a7b9a4"
json_file_path = f"abfss://DataCeili@onelake.dfs.fabric.microsoft.com/Bronze.Lakehouse/Files/{path}/*.json"

#Read JSON to a dataframe
df_breweries = spark.read.format('json').option('multiline',False).load(json_file_path)
display(df_breweries)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import lit
#Add loaddate and runid
loaddate = "/".join(path.split("/")[:3])
loadrunid = path.split("/")[-1]

df_breweries_enriched = df_breweries.withColumns({"_loaddate": lit(loaddate), "_loadrunid": lit(loadrunid)})
display(df_breweries_enriched)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Write breweries to Silver Layer
df_breweries_enriched.write.format("delta").mode("overwrite").saveAsTable("Silver.clean_breweries")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
