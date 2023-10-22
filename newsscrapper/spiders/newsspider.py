import scrapy


class NewsspiderSpider(scrapy.Spider):
    name = "newsspider"
    allowed_domains = ["veekshanam.com"]
    start_urls = ["https://veekshanam.com/"]

    def parse(self, response):
        headings = response.css('div.mvp-feat1-list-out.relative')
        for news in headings:
            yield{
                'news' : news.css('h2::text').get()
            }