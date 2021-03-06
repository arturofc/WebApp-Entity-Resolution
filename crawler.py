from entity import EntityItem
import json
import scrapy


class SosWebAppCrawler(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['firststop.sos.nd.gov']
    entity_search_api_url = 'https://firststop.sos.nd.gov/api/Records/businesssearch'
    entity_info_api_base = 'https://firststop.sos.nd.gov/api/FilingDetail/business'
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
        entities = EntityItem()
        raw_data = json.loads(response.body_as_unicode())

        for key, data in raw_data['rows'].items():
            yield scrapy.Request(
                method='GET',
                url=f"{self.entity_info_api_base}/{key}/false",
                callback=self.get_entity_info,
                headers=self.headers,
                meta={'entities': entities, 'name': data['TITLE'][0]}
            )

    def get_entity_info(self, response):
        entities = response.meta['entities']
        entities['entity_name'] = response.meta['name']
        entities['comm_registered_agent'] = None
        entities['registered_agent'] = None
        entities['owner'] = None
        raw_data = json.loads(response.body_as_unicode())

        for element in raw_data['DRAWER_DETAIL_LIST']:
            label = element['LABEL']

            if label == 'Commercial Registered Agent':
                entities['comm_registered_agent'] = element['VALUE']
            elif label == 'Registered Agent':
                entities['registered_agent'] = element['VALUE']
            elif label == 'Owner Name':
                entities['owner'] = element['VALUE']

        yield entities
