from entity import EntityItem
import json
import scrapy


class SosWebAppCrawler(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['firststop.sos.nd.gov']
    entity_search_api_url = 'https://firststop.sos.nd.gov/api/Records/businesssearch'
    entity_info_api = ''
    headers = {
        'Content-Type': 'application/json',
        'charset': 'UTF-8',
        'Accept': 'application/json'
    }

    def start_requests(self):
        payload = {
            "SEARCH_VALUE": "X",
            "STARTS_WITH_YN": "true",
            "ACTIVE_ONLY_YN": "true"
        }
        yield scrapy.Request(
            method='POST',
            url=self.entity_search_api_url,
            callback=self.search_entities,
            body=json.dumps(payload),
            headers=self.headers
        )

    def search_entities(self, response):
        form_data = {}
        entities = EntityItem()
        raw_data = json.loads(response.body_as_unicode())

        for key in raw_data['rows']:
            entities['entity_id'] = key
            yield entities
