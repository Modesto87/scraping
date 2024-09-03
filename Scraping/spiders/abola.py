# abola.py
import scrapy
from datetime import datetime


class AbolaSpider(scrapy.Spider):
    name = "abola"
    start_urls = ['https://www.abola.pt/']

    def parse(self, response):
        for article in response.css('div.card.news-item.top-item'):
            yield {
                'title': article.css('.titulo.ellipsis-2-line::text').get(),
                'image_link': article.css('img.side-article::attr(src)').get(),
                'source_link': article.css('.noticia-item-image::attr(href)').get(),
                'date_added': datetime.utcnow()
            }
