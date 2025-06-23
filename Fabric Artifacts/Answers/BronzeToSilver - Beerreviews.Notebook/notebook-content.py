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
# META         },
# META         {
# META           "id": "f16dbefd-294c-417f-b27c-c41f65613232"
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

# # Bronze To Silver - Beerreviews

# MARKDOWN ********************

# In this notebook, data from the Bronze Layer is cleansed and stored in the Silver Lakehouse. The follwing cleaning steps are applied:
# - api_breweries -> cleansed_breweries: Remove duplicates
# - adls_beerreviews -> cleansed_beerreviews: add brewery ID through name matching and drop reviews where the brewery ID is null
# - azsql_beerconsumption -> cleansed_beerconsumption: drop irrelevant columns
# - pg_worldhappinessindex -> cleansed_worldhappinessindex: drop irrelevant columns

# CELL ********************

#Load breweries into a dataframe
df_breweries_prep = spark.sql("SELECT * FROM Silver.clean_breweries")

#Load reviews into a dataframe
df_reviews = spark.sql("SELECT * FROM Bronze.adls_beerreviews")
display(df_reviews)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Filter columns and breweries and breweries in reviews
df_breweries_prep = df_breweries_prep.select("id", "name")
df_reviews_prep = df_reviews.select("brewery_id", "brewery_name").dropDuplicates(["brewery_name"])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Count unique breweries
count_df_breweries_prep = df_breweries_prep.count()
print("unique breweries:", count_df_breweries_prep)

#Count unique breweries in reviews
count_df_reviews_prep = df_reviews_prep.count()
print("unique breweries in reviews:",count_df_reviews_prep)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#levenshtein Fuzzymatching
from pyspark.sql.functions import levenshtein, col
df_cross = df_breweries_prep.crossJoin(df_reviews_prep)
df_result = df_cross.withColumn("lev_distance", levenshtein(col("name"), col("brewery_name")))

# Filter for matches within a threshold
threshold = 1
df_matches = df_result.filter(df_result.lev_distance <= threshold)

#Display result
display(df_matches)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Count the matches
df_matches.count()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Filter out rows with wrong matching
df_matches_filtered = df_matches.filter(~df_matches['brewery_id'].isin([12560, 20009, 26817, 26528, 2594, 4922, 24822, 13165, 16813])).drop("brewery_name","name")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Join the brewery_id withthe to reviews
from pyspark.sql.functions import broadcast
df_reviews_enriched = df_reviews.join(broadcast(df_matches_filtered), on="brewery_id", how="left")
display(df_reviews_enriched)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#from pyspark.sql.functions import col
# Count rows where id is null
# null_count = df_reviews_enriched.filter(col("id").isNull()).count()
# Count rows where id is not null
#not_null_count = df_reviews_enriched.filter(col("id").isNotNull()).count()

#print(f"Rows where id is null: {null_count}")
#print(f"Rows where id is not null: {not_null_count}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Drop columns and rename
from pyspark.sql.functions import col, lit
loaddate = "/".join(path.split("/")[:3])
loadrunid = path.split("/")[-1]

df_result_reviews = (
    df_reviews_enriched
    .drop("brewery_id", "lev_distance", "brewery_name") # Drop columns
    .withColumnsRenamed({'id': 'brewery_id', 'beer_beerid': 'beer_id'}) # Rename id to brewery_id
    .withColumns({"_loaddate": lit(loaddate), "_loadrunid": lit(loadrunid)}) #Add loaddate and runid
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Display result
display(df_result_reviews)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

#Write reviews to Silver Layer
df_result_reviews.write.format("delta").mode("overwrite").saveAsTable("Silver.clean_beerreviews")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
