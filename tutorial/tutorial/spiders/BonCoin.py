#######################
##
##  This module allow to manipulate information in LeBonCoin.fr
##
#######################

#'https://www.leboncoin.fr/locations/1464398382.htm/'
#https://www.leboncoin.fr/_immobilier_/offres/


import scrapy


class LeBonCoinSpider(scrapy.Spider):
    name = "leboncoin"

    def start_requests(self):
        urls = [
            'https://www.leboncoin.fr/locations/1464398382.htm/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        yield {
            'City' : response.xpath('//div[@class="_1aCZv"]//text()').extract()[0],
            'Zipcode' : response.xpath('//div[@class="_1aCZv"]//text()').extract()[2],
            'type' :  response.xpath('//div[@class="_3Jxf3"]/text()').extract()[1],
            'price' : response.xpath('//span[@class="_1F5u3"]/text()').extract_first(),
            'empty' :  response.xpath('//div[@class="_3Jxf3"]/text()').extract()[3],
            'surface' :  response.xpath('//div[@class="_3Jxf3"]/text()').extract()[4],
            'chargeincluded' :  response.xpath('//div[@class="_3Jxf3"]/text()').extract()[0],
            'reference' :  response.xpath('//div[@class="_3Jxf3"]/text()').extract()[5],
            'description' : response.xpath('//span[@class="_2wB1z"]/text()').extract()
            
            }
"""            
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
"""
