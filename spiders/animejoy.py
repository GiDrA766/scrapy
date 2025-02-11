import scrapy

from ..items import AnimeItem

class AnimejoySpider(scrapy.Spider):
    name = "animejoy"
    allowed_domains = ["animejoy.ru"]
    start_urls = ["https://animejoy.ru"]

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
        listofgenres = desc[1].css("span")
        genres = []
        for genre in listofgenres:
            genres.append(genre.css("::text").get())
            
        
        anime["name"] = response.xpath("//div[@class='titleup']/h1/text()").get()
        anime["season"] = desc[0].css("a::text").get()
        anime["genres"] = genres
        anime["country"] = desc[2].css("span")[1].css("::text").get()
        anime["date_of_production"] =  desc[4].xpath("text()").get().strip()
        anime["director"] = desc[5].css("a::text").get()
        anime["scenario"] = desc[6].css("a::text").get()
        anime["studio"] = desc[7].css("a::text").get()
        anime["age_rating"] = desc[8].xpath("text()").get().strip()

        yield anime
        
        
