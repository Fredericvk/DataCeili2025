CREATE PROCEDURE sp_create_gold_beerreviews
AS
BEGIN
    -- Drop the table if it exists
    IF OBJECT_ID('Gold.dbo.gold_beerreviews', 'U') IS NOT NULL
    BEGIN
        TRUNCATE TABLE Gold.dbo.gold_beerreviews;
    END;

    -- Create the table from the source
    INSERT INTO dbo.gold_beerreviews
    SELECT * FROM Silver.dbo.clean_beerreviews WHERE brewery_id IS NOT NULL;

    ALTER TABLE gold_beerreviews ADD CONSTRAINT FK_gold_beerreviews FOREIGN KEY (brewery_id) REFERENCES gold_breweries (id) NOT ENFORCED;
END;