# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookstorescrapingItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class AnimeItem(scrapy.Item):
    name = scrapy.Field()
    season = scrapy.Field()
    genres = scrapy.Field()
    country = scrapy.Field()
    date_of_production = scrapy.Field()
    director = scrapy.Field()
    scenario = scrapy.Field()
    studio = scrapy.Field()
    age_rating = scrapy.Field()
    