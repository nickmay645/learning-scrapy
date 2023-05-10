import scrapy
import logging
import os

class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        
        """
        This function parses a sample response. Some contracts are mingled
        with this docstring.

        @url https://www.worldometers.info/world-population/population-by-country/
        @returns items 0 0
        @returns requests 10
        """

        countries = response.xpath("//td/a")
        
        for country in countries:        
            
            country_name = country.xpath(".//text()").get()
            country_link = country.xpath(".//@href").get()

            yield response.follow(url=country_link, callback=self.parse_country, meta={'country_name': country_name})


    def parse_country(self, response):
        
        """
        This function parses a sample response. Some contracts are mingled
        with this docstring.

        @url https://www.worldometers.info/world-population/china-population/
        @returns items 15
        @returns requests 0 0
        @scrapes country_name year population
        """

        if os.environ.get("SCRAPY_CHECK"):
            country_name = 'China'
        else:
            country_name = response.request.meta['country_name']

        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        
        for row in rows:
            
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[1]/text()").get()
            
            yield {
                "country_name": country_name,
                "year": year,
                "population": population
            }
