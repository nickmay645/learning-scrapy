import scrapy
import json

class GdpDebtSpider(scrapy.Spider):
    name = "gdp_debt"
    allowed_domains = ["worldpopulationreview.com"]
    start_urls = ["https://worldpopulationreview.com/country-rankings/countries-by-national-debt"]

    def parse(self, response):
        next_data = response.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
        json_data = json.loads(next_data)
        listings = json_data['props']['pageProps']['listing']
        for listing in listings:
            yield {
                'country': listing.get('country'),
                'gdp_debt': listing.get('debtPercGdp')
            }
