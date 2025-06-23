DROP TABLE IF EXISTS dbo.gold_breweries
GO;

CREATE TABLE dbo.gold_breweries (
    address_1 VARCHAR(255) NULL,
    address_2 VARCHAR(255) NULL,
    address_3 VARCHAR(255) NULL,
    brewery_type VARCHAR(100) NULL,
    city VARCHAR(100) NULL,
    country VARCHAR(100) NOT NULL,
    id VARCHAR(50) NOT NULL,
    latitude FLOAT NULL,
    longitude FLOAT NULL,
    name VARCHAR(255) NULL,
    phone VARCHAR(50) NULL,
    postal_code VARCHAR(20) NULL,
    state VARCHAR(100) NULL,
    state_province VARCHAR(100) NULL,
    street VARCHAR(255) NULL,
    website_url VARCHAR(255) NULL,
    _loaddate VARCHAR(50) NULL,
    _loadrunid VARCHAR(50) NULL
);

INSERT INTO dbo.gold_breweries
SELECT * FROM Silver.dbo.clean_breweries
GO;