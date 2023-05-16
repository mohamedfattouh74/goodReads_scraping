import scrapy


class SpGoodreadsSpider(scrapy.Spider):
    name = "sp_goodReads"
    allowed_domains = ["www.goodreads.com"]
    start_urls = ["https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century"]

    def parse(self, response):

        books=response.xpath("//td/a")

        for book in books:
            link=book.xpath(".//@href").get()
            yield response.follow(url=link, callback=self.parse_books)

        pagination = response.xpath("//div[@class='pagination']")
        next_page_url = pagination.xpath(".//a[@class='next_page']/@href").get()

        if next_page_url:
            yield response.follow(url=next_page_url, callback=self.parse)

    def parse_books(self,response):

        title=response.xpath("//h1/text()").get()
        writer=response.xpath("//div[@class='ContributorLinksList']/span[1]/a/span/text()").get()
        rating=response.xpath("//div[@class='BookPageMetadataSection__ratingStats']//div[@class='RatingStatistics__rating']/text()").get()
        no_ratings=response.xpath("//div[@class='BookPageMetadataSection__ratingStats']//span[@data-testid='ratingsCount']/text()").get()
        genre=response.xpath("//ul[@aria-label='Top genres for this book']/span/span[2]/a/span/text()").get()
        no_pages=response.xpath("//div[@class='FeaturedDetails']/p[1]/text()").get()
        publish_date = response.xpath("//div[@class='FeaturedDetails']/p[2]/text()").get()

        yield{
            "title":title,
            "writer":writer,
            "rating":rating,
            "no_ratings":no_ratings,
            "genre":genre,
            "no_pages":no_pages,
            "publish_date":publish_date,
        }



