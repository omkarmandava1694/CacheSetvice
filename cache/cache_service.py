
from collections import OrderedDict
import logging
from .entity import Entity

class CacheService:
    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = OrderedDict()
        self.database = {}

        logging.basicConfig(
            filename='logs/log.txt',
            level=logging.INFO,
            format='%(asctime)s:%(levelname)s:%(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def add(self, entity):
        entity_id = entity.getId()
        if entity_id in self.cache:
            self.cache.move_to_end(entity_id)
        else:
            if len(self.cache) >= self.max_size:
                evicted_id, evicted_entity = self.cache.popitem(last=False)
                self.database[evicted_id] = evicted_entity
                self.logger.info(f"Evicted Entity ID: {evicted_id} to database")
            self.cache[entity_id] = entity

    def get(self, entity):
        entity_id = entity.getId()
        if entity_id in self.cache:
            self.cache.move_to_end(entity_id)
            return self.cache[entity_id]
        elif entity_id in self.database:
            self.logger.info(f"Entity ID: {entity_id} retrieved from database")
            return self.database[entity_id]
        else:
            self.logger.warning(f"Entity ID: {entity_id} not found")
            return None

    def remove(self, entity):
        entity_id = entity.getId()
        self.cache.pop(entity_id, None)
        self.database.pop(entity_id, None)
        self.logger.info(f"Removed Entity ID: {entity_id} from cache and database")

    def removeAll(self):
        self.cache.clear()
        self.database.clear()
        self.logger.info("Removed all entities from cache and database")

    def clear(self):
        self.cache.clear()
        self.logger.info("Cleared internal cache")
