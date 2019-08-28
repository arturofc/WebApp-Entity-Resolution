import scrapy


class EntityItem(scrapy.Item):
    entity_name = scrapy.Field()
    comm_registered_agent = scrapy.Field()
    registered_agent = scrapy.Field()
    owner = scrapy.Field()
