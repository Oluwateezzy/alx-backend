#!/usr/bin/python3
""" BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """fifo caching """
    def __init__(self):
        """ initialize"""
        super().__init__()

    def put(self, key, item):
        """put method"""
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = sorted(self.cache_data)[0]
            self.cache_data.pop(oldest_key)
            print("DISCARD: {}".format(oldest_key))

    def get(self, key):
        """get method"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
