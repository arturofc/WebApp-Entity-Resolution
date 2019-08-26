import scrapy


class EntityItem(scrapy.Item):
    entity_id = scrapy.Field()
    comm_registered_entity = scrapy.Field()
    registered_agent = scrapy.Field()
    owners = scrapy.Field()
