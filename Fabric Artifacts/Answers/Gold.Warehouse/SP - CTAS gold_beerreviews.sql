CREATE PROCEDURE sp_create_gold_beerreviews
AS
BEGIN
    -- Drop the table if it exists
    IF OBJECT_ID('Gold.dbo.gold_beerreviews', 'U') IS NOT NULL
    BEGIN
        DROP TABLE Gold.dbo.gold_beerreviews;
    END;

    -- Create the table from the source
    SELECT *
    INTO Gold.dbo.gold_beerreviews
    FROM Silver.dbo.clean_beerreviews
    WHERE brewery_id IS NOT NULL;
END;
GO