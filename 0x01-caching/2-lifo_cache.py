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
        """put method"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            latest_key = sorted(self.cache_data)[-2]
            self.cache_data.pop(latest_key)
            print(latest_key)
    
    def get(self, key):
        """get method """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
