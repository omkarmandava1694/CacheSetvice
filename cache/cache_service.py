
from collections import OrderedDict
import logging
from .entity import Entity

class CacheService:
    def __init__(self, max_size):
        # Set the maximum size for the cache
        self.max_size = max_size
        # Initialize the cache using OrderDict to maintain LRU order
        self.cache = OrderedDict()
        # Creating a dummy database to store evicted items
        self.database = {}

        # Configure loggings to track cache operations
        logging.basicConfig(
            filename='logs/log.txt',
            level=logging.INFO,
            format='%(asctime)s:%(levelname)s:%(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def add(self, entity):
        entity_id = entity.getId()
        # If the entity already exists in the cache, move it to the end(most recently used)
        if entity_id in self.cache:
            self.cache.move_to_end(entity_id)
        else:
            # If cache exceeds max size, evict the least recently used (LRU) item
            if len(self.cache) >= self.max_size:
                evicted_id, evicted_entity = self.cache.popitem(last=False)
                self.database[evicted_id] = evicted_entity
                self.logger.info(f"Evicted Entity ID: {evicted_id} to database")
            # Add the new entity to the cache    
            self.cache[entity_id] = entity

    def get(self, entity):
        # If entity is in cache, return it and update its usage
        entity_id = entity.getId()
        if entity_id in self.cache:
            self.cache.move_to_end(entity_id)
            return self.cache[entity_id]
        # If entity is in database, log and return it
        elif entity_id in self.database:
            self.logger.info(f"Entity ID: {entity_id} retrieved from database")
            return self.database[entity_id]
        else:
            # Updating the log with not found message
            self.logger.warning(f"Entity ID: {entity_id} not found")
            return None

    def remove(self, entity):
        # Removes a specific entity from both cache and the dummy database
        entity_id = entity.getId()
        self.cache.pop(entity_id, None)
        self.database.pop(entity_id, None)
        self.logger.info(f"Removed Entity ID: {entity_id} from cache and database")

    def remove_all(self):
        # Clears all the entries from both the cache and the simulated database
        self.cache.clear()
        self.database.clear()
        self.logger.info("Removed all entities from cache and database")

    def clear(self):
        #clear only the internal cache
        self.cache.clear()
        self.logger.info("Cleared internal cache")

    def cache_size(self):
        return len(self.cache)
    
    def db_size(self):
        return self.database.size()


