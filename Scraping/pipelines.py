# pipelines.py
from Scraping.models import NewsArticle, engine
from sqlalchemy.orm import sessionmaker

class NewsPipeline:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        news_article = NewsArticle(
            title=item["title"],
            image_link=item.get("image_link"),
            source_link=item["source_link"],
            date_added=item["date_added"]
        )

        try:
            session.add(news_article)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item