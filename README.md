# IMDB Best Movies Scraper
This is a web scraper written in Python using Scrapy, a Python framework for web scraping.

The purpose of this scraper is to extract information about the best rated movies on IMDB. The information extracted includes the movie title, year of release, IMDB rating, and number of user votes.

## Installation
Before you can run this scraper, you need to have Scrapy installed on your computer. If you don't have it installed, you can install it using pip:

*pip install scrapy*

## Usage
To run the scraper, navigate to the root directory of the project and run the following command:

*scrapy crawl imdb*

By default, the scraper will output the results to the console. If you want to save the results to a file, you can pass the output_file argument when running the scraper:

*scrapy crawl imdb-best-movies -a output_file=output.json*

This will save the results to a file named output.json in the root directory of the project.

## Customization
If you want to customize the scraper, you can modify the following files:

- imdbv1/spiders/imdb_best_movies_spider.py: This file contains the spider that defines how to extract the information from the website.
- imdbv1/items.py: This file defines the data structure for the scraped items.
- imdbv1/pipelines.py: This file contains the pipeline that defines how to process the scraped items.
