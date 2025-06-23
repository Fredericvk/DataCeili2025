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

# # BronzeToSilver - Join WorldHappinessindex and WorldBeerConsumption

# CELL ********************

#Define loaddate and loadrunid
loaddate = "/".join(path.split("/")[:3])
loadrunid = path.split("/")[-1]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Clean Worldhappinessindex

# CELL ********************

# Load worldhappinessindex
df_worldhappinessindex = spark.sql("SELECT * FROM Bronze.pg_worldhappiness_index")
display(df_worldhappinessindex)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Enrich worldhappinessindex
df_worldhappinessindex_filtered = df_worldhappinessindex.drop("happiness_rank_2024", "happiness_score_2024","id")
display(df_worldhappinessindex_filtered)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ## Join with beerconsumption

# CELL ********************

df_beerconsumption = spark.sql("SELECT * FROM Bronze.azsql_beerconsumption")
df_beerconsumption =df_beerconsumption.withColumnsRenamed({"flagCode": "flag_code", "BeerConsumption_TotalConsumption_tonnes_2022": "totalbeerconsumption_2022_1000L","BeerConsumption_ConsumptionPerCapita_KgPerCapita_2022":"beerconsumptionpercapita_2022_L"}).drop("country")
display(df_beerconsumption)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import lit
df_worlddata = (
    df_worldhappinessindex_filtered
    .join(df_beerconsumption, on='flag_code', how='inner') #join with worldhappinessindex
    .withColumns({"_loaddate": lit(loaddate), "_loadrunid": lit(loadrunid)}) #Add loaddate and runid
    )
display(df_worlddata)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Save table to Silver Layer
df_worlddata.write.format("delta").mode("overwrite").saveAsTable("Silver.clean_worlddata")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark",
# META   "frozen": true,
# META   "editable": false
# META }
