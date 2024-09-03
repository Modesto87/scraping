from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Scraping.spiders.abola import AbolaSpider
from Scraping.spiders.correiodamanha import CorreioDaManhaSpider

process = CrawlerProcess(get_project_settings())

# Adicione os spiders que deseja executar.
process.crawl(AbolaSpider)
process.crawl(CorreioDaManhaSpider)

# Inicie a execução dos spiders
process.start()
