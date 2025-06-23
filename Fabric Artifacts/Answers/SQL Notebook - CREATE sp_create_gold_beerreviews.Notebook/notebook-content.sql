-- Fabric notebook source

-- METADATA ********************

-- META {
-- META   "kernel_info": {
-- META     "name": "sqldatawarehouse"
-- META   },
-- META   "dependencies": {
-- META     "warehouse": {
-- META       "default_warehouse": "8c711f7b-7549-9fda-471e-5c360fe02c6f",
-- META       "known_warehouses": [
-- META         {
-- META           "id": "8c711f7b-7549-9fda-471e-5c360fe02c6f",
-- META           "type": "Datawarehouse"
-- META         }
-- META       ]
-- META     }
-- META   }
-- META }

-- CELL ********************

-- Check if the procedure already exists
IF OBJECT_ID('dbo.sp_create_gold_beerreviews', 'P') IS NOT NULL
BEGIN
    PRINT 'Procedure exists.'
END
ELSE
BEGIN
    -- Create the procedure dynamically
    EXEC('
        CREATE PROCEDURE dbo.sp_create_gold_beerreviews
        AS
        BEGIN
            -- If the target table exists, truncate it
            IF OBJECT_ID(''Gold.dbo.gold_beerreviews'', ''U'') IS NOT NULL
            BEGIN
                TRUNCATE TABLE Gold.dbo.gold_beerreviews;
            END

            -- Insert data from the source table
            INSERT INTO Gold.dbo.gold_beerreviews
            SELECT * FROM Silver.dbo.clean_beerreviews
            WHERE brewery_id IS NOT NULL;

            -- Add a foreign key constraint (not enforced)
            ALTER TABLE Gold.dbo.gold_beerreviews
            ADD CONSTRAINT FK_gold_beerreviews FOREIGN KEY (brewery_id)
            REFERENCES Gold.dbo.gold_breweries(id) NOT ENFORCED;
        END
    ');
END

-- METADATA ********************

-- META {
-- META   "language": "sql",
-- META   "language_group": "sqldatawarehouse"
-- META }

-- CELL ********************

SELECT * FROM gold_beerreviews

-- METADATA ********************

-- META {
-- META   "language": "sql",
-- META   "language_group": "sqldatawarehouse"
-- META }

-- CELL ********************


-- METADATA ********************

-- META {
-- META   "language": "sql",
-- META   "language_group": "sqldatawarehouse"
-- META }
