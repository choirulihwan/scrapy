# Step by Step Scrapy

[INSTALL]
- pip install scrapy

[CREATE PROJECT]
- scrapy startproject [project_name]

[CREATE SPIDER FOR WEBSITE TARGET]
- scrapy genspider [spider_name] [url]
- scrapy genspider rwid 167.172.70.208:9999 /*rwid (example)*/


[START SCRAPING]
- scrapy crawl [spider_name]

[START SCRAPING OUTPUT csv]
- scrapy crawl [spider] -o [file].csv

[START SCRAPING IN SHELL]
- scrapy shell [url]