#!/usr/bin/python3
""" BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Lifo caching """
    def __init__(self):
        """ initialize"""
        super().__init__()
    
    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_item)
            print('DISCARD:', self.last_item)
        if key:
            self.last_item = key
    
    def get(self, key):
        """get method """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
