import scrapy


class BoatEarpodsSpider(scrapy.Spider):
    name = 'boat_earpods'
    allowed_domains = ['amazon.in']
    handle_httpstatus_all = True
    start_urls = [
        'https://www.amazon.in/s?k=earpods+boat+wireless&crid=DSA39D6DROEP&sprefix=ear%2Caps%2C393&ref=nb_sb_ss_ts-doa-p_6_3']

    def parse(self, response):
        for row in response.xpath("//div[@class='s-include-content-margin s-border-bottom s-latency-cf-section']"):
            price = row.xpath(".//span[@class='a-price-whole']/text()").get()
            original_price = row.xpath(
                ".//span[@class='a-price a-text-price']/span/following-sibling::span/text()").get().strip('\u20b9')
            discount = row.xpath(
                ".//span[@class='a-letter-space']/following-sibling::span/text()").get().split('\u20b9')[1]

            yield{
                'product_name': row.xpath(".//h2//span[@class='a-size-medium a-color-base a-text-normal']/text()").get(),
                'product_price': 'Not available' if price == None else f'Rs{price}',
                'product_original_price': 'Not available' if original_price == None else f'Rs{original_price}',
                'discount': discount

            }
