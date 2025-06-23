CREATE TABLE [dbo].[gold_breweries] (

	[address_1] varchar(255) NULL, 
	[address_2] varchar(255) NULL, 
	[address_3] varchar(255) NULL, 
	[brewery_type] varchar(100) NULL, 
	[city] varchar(100) NULL, 
	[country] varchar(100) NOT NULL, 
	[id] varchar(50) NOT NULL, 
	[latitude] float NULL, 
	[longitude] float NULL, 
	[name] varchar(255) NULL, 
	[phone] varchar(50) NULL, 
	[postal_code] varchar(20) NULL, 
	[state] varchar(100) NULL, 
	[state_province] varchar(100) NULL, 
	[street] varchar(255) NULL, 
	[website_url] varchar(255) NULL, 
	[_loaddate] varchar(50) NULL, 
	[_loadrunid] varchar(50) NULL
);


GO
ALTER TABLE [dbo].[gold_breweries] ADD CONSTRAINT PK_goldbreweriesid primary key NONCLUSTERED ([id]);
GO
ALTER TABLE [dbo].[gold_breweries] ADD CONSTRAINT FK_goldbreweriescountry FOREIGN KEY ([country]) REFERENCES [dbo].[gold_worlddata]([country]);