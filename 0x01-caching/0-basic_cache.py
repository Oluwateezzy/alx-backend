#!/usr/bin/python3
""" 0-main """
""" BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def init(self):
        """ Initiliaze """
        super().__init__()
    
    def put(self, key, item):
        """put function"""
        if key and item:
            self.cache_data[key] = item
    
    def get(self, key):
        """get function"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
