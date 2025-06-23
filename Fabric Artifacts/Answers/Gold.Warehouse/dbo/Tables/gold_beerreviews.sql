CREATE TABLE [dbo].[gold_beerreviews] (

	[review_time] int NULL, 
	[review_overall] float NULL, 
	[review_aroma] float NULL, 
	[review_appearance] float NULL, 
	[review_profilename] varchar(255) NULL, 
	[beer_style] varchar(255) NULL, 
	[review_palate] float NULL, 
	[review_taste] float NULL, 
	[beer_name] varchar(255) NULL, 
	[beer_abv] float NULL, 
	[beer_id] int NULL, 
	[brewery_id] varchar(50) NOT NULL, 
	[_loaddate] varchar(255) NULL, 
	[_loadrunid] varchar(255) NULL
);


GO
ALTER TABLE [dbo].[gold_beerreviews] ADD CONSTRAINT FK_gold_beerreviews FOREIGN KEY ([brewery_id]) REFERENCES [dbo].[gold_breweries]([id]);