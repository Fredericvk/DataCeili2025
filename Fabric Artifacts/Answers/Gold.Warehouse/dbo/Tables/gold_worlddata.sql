CREATE TABLE [dbo].[gold_worlddata] (

	[flag_code] varchar(10) NULL, 
	[country] varchar(100) NOT NULL, 
	[latest_score_change] decimal(5,3) NULL, 
	[happiness_rank_2022] int NULL, 
	[happiness_score_2022] decimal(4,3) NULL, 
	[totalbeerconsumption_2022_1000L] bigint NULL, 
	[beerconsumptionpercapita_2022_L] decimal(6,2) NULL, 
	[_loaddate] varchar(50) NULL, 
	[_loadrunid] varchar(50) NULL
);


GO
ALTER TABLE [dbo].[gold_worlddata] ADD CONSTRAINT PK_country primary key NONCLUSTERED ([country]);