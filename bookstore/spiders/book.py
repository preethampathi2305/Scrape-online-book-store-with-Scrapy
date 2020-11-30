import scrapy

class bookspider(scrapy.Spider):
    name="book_spider"
    def start_requests(self):
        urls=['http://books.toscrape.com/']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self, response, **kwargs):
        page=response.url.split("/")[-1]
        filename='bookpage-%s.html'%page
        for b in response.css("article.product_pod"):
            img_url=b.css("img.thumbnail::attr(src)").get()
            title=b.css("img.thumbnail::attr(alt)").get()
            price=b.css("p.price_color::text").get()
            print(img_url,title,price)
            yield {
                'image_url':img_url,
                'book_title':title,
                'product_price':price,
            }
        npage=response.css("li.next a::attr(href)").get()
        if npage is not None:
            npage=response.urljoin(npage)
            yield scrapy.Request(npage,callback=self.parse)