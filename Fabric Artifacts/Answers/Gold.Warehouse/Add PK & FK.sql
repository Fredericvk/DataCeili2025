-- add primary key to world data
ALTER TABLE gold_worlddata ADD CONSTRAINT PK_country PRIMARY KEY NONCLUSTERED (country) NOT ENFORCED;

-- add primary and foreign key to gold_breweries
ALTER TABLE gold_breweries ADD CONSTRAINT PK_goldbreweriesid PRIMARY KEY NONCLUSTERED (id) NOT ENFORCED;
ALTER TABLE gold_breweries ADD CONSTRAINT FK_goldbreweriescountry FOREIGN KEY (country) REFERENCES gold_worlddata (country) NOT ENFORCED;


-- add foreign key to gold_beerreviews
CREATE TABLE [Gold].[dbo].[gold_beerreviews_pk]
(
	[review_time] [int] NULL,
	[review_overall] [float] NULL,
	[review_aroma] [float] NULL,
	[review_appearance] [float] NULL,
	[review_profilename] [varchar](255) NULL,
	[beer_style] [varchar](255) NULL,
	[review_palate] [float] NULL,
	[review_taste] [float] NULL,
	[beer_name] [varchar](255) NULL,
	[beer_abv] [float] NULL,
	[beer_id] [int] NULL,
	[brewery_id] [varchar](50) NOT NULL,
	[_loaddate] [varchar](255) NULL,
	[_loadrunid] [varchar](255) NULL
)
GO

INSERT INTO dbo.gold_beerreviews_pk
SELECT * FROM dbo.gold_beerreviews
GO

DROP TABLE IF EXISTS [Gold].[dbo].[gold_beerreviews]
GO

EXEC sp_rename 'dbo.gold_beerreviews_pk', 'gold_beerreviews'
GO

ALTER TABLE gold_beerreviews ADD CONSTRAINT FK_gold_beerreviews FOREIGN KEY (brewery_id) REFERENCES gold_breweries (id) NOT ENFORCED;