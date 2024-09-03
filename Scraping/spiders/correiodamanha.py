import scrapy
from datetime import datetime


class CorreioDaManhaSpider(scrapy.Spider):
    name = "cm"
    start_urls = ['https://www.cmjornal.pt/']

    def parse(self, response):
        for article in response.css('div.card.news-item.top-item'):
            yield {
                'title': article.css('.destaque.with_label a span::text').get(),
                'image_link': article.css('.figure_container .image img::attr(src)').get(),
                'source_link': article.css('.figure_container a::attr(href)').get(),
                'date_added': datetime.utcnow()
            }