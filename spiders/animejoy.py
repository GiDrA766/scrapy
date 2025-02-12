from time import sleep
import scrapy

from ..items import AnimeItem

class AnimejoySpider(scrapy.Spider):
    name = "animejoy"
    allowed_domains = ["animejoy.ru"]
    start_urls = ["https://animejoy.ru/"]
    def parse(self, response):
        items = response.xpath("//div[@id = 'dle-content']//article")[1:]
        for item in items:
            url = item.css("a::attr(href)").get()
            yield response.follow(url, self.parse_page )
        # next = response.css("span.page_next a::attr(href)").get()
        # if next is not None:
        #     yield response.follow(next, self.parse)  # Increment the page number for the next request.
        
    
    
    def parse_page(self, response):
        
        anime = AnimeItem()
        desc = response.css("div.blkdesc p")
        # listofgenres = desc[1].css("span")[1:]
        # genres = []
        # for genre in listofgenres:
        #     genres.append(genre.css("::text").get())
            
        anime["name"] = response.xpath("//div[@class='titleup']/h1/text()").get(default=None)
        
        # season_year = desc[0].css("a::text").get(default=None)
        # if season_year:
        #     anime["season"], anime["year"] = (season_year.split('-') + [None, None])[:2]
        # else:
        #     anime["season"], anime["year"] = None, None
        # anime["genres"] = genres  # Assuming genres is already defined
        # anime["country"] = desc[2].css("span:nth-child(2)::text").get(default=None)
        # anime["date_of_production"] = desc[4].xpath("text()").get(default="").strip() if desc[4].xpath("text()").get() else None
        # anime["director"] = desc[5].css("a::text").get(default=None)
        # anime["scenario"] = desc[6].css("a::text").get(default=None)
        # anime["studio"] = desc[7].css("a::text").get(default=None)
        # try:
        #     anime["age_rating"] = desc[8].xpath("text()").get(default="").strip() if desc[8].xpath("text()").get() else None
        # except:
        #     anime["age_rating"] = desc[7].xpath("text()").get(default="").strip() if desc[8].xpath("text()").get() else None
        # yield anime
        
        for row in desc:
            try:
                title = row.css("span::text").get()[:-1]
            except:
                continue
            if title == "Сезон":
                season_year = row.css("a::text").get(default=None)
                if season_year:
                    anime["season"], anime["year"] = (season_year.split('-') + [None, None])[:2]
                else:
                    anime["season"], anime["year"] = None, None
            if title == "Жанр":
                listofgenres = row.css("span")[1:]
                genres = []
                for genre in listofgenres:
                    genres.append(genre.css("::text").get())
                anime["genres"] = genres  # Assuming genres is already defined
            if title == "Страна":
                anime["country"] = row.css("span:nth-child(2)::text").get(default=None)
            if title == "Дата выпуска":
                anime["date_of_production"] = row.xpath("text()").get(default="").strip() if desc[4].xpath("text()").get() else ""
            if title == "Режиссер":
                anime["director"] = row.css("a::text").get(default=None)
            if title == "Сценарий":
                anime["scenario"] = row.css("a::text").get(default=None)
            if title == "Студия":
                anime["studio"] = row.css("a::text").get(default=None)
            if title == "Воз. рейтинг":
                anime["age_rating"] = row.xpath("text()").get(default="").strip() if row.xpath("text()").get() else None
                
        yield anime 
        
