# Created an Entity class to represent a data object with an id and associated data 
class Entity:
    def __init__(self, entity_id, data):
        # Initialize the entry with unique id and its data
        self.id = entity_id
        self.data = data

    def getId(self):
        return self.id
