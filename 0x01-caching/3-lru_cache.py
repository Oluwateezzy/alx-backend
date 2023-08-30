#!/usr/bin/python3
""" BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ Least Recently used """

    def __init__(self):
        """ Initialized """
        super().__init__()
        self.cache_data = OrderedDict()
    
    def put(self, key, item):
        """ put method """
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru = self.cache_data.popitem(last=False)
            print('DISCARD:', lru[0])
    
    def get(self, key):
        """ Get method """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
