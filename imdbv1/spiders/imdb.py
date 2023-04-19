import scrapy


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    allowed_domains = ["www.imdb.com"]

    User_agent = " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.imdb.com/chart/top/?ref_=nv_mv_250",
            headers={
                "User-Agent": self.User_agent
            }
        )

    def parse(self, response):
        for movie in response.xpath("//tbody/tr/td[@class='titleColumn']"):
            data = {
                "order": movie.xpath("normalize-space(.//text()[1])").get(),
                "name": movie.xpath(".//a/text()").get(),
                "link": movie.xpath(".//a/@href").get(),
                "year": movie.xpath("normalize-space(substring-before(substring-after(.//span, '('), ')'))").get(),
            }

            yield response.follow(url=data['link'], callback=self.parse_movie, meta=data,
                                  headers={
                "User-Agent": self.User_agent,
            }
            )

    def parse_movie(self, response):
        yield {
            "order": response.request.meta["order"],
            "name": response.request.meta["name"],
            "link": f'www.imdb.com{response.request.meta["link"]}',
            "year": response.request.meta["year"],
            "rating": response.xpath('(//div/*[contains(@class, " iZlgcd")])[1]/text()').get(),
            "about": response.xpath('(//p/span[contains(@class, " cxqNYC")])[1]/text()').get(),
            "category": ", ".join(response.xpath("//div[@class='ipc-chip-list__scroller']//span/text()[normalize-space()]").getall()),
        }
