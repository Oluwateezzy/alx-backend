#!/usr/bin/python3
""" BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ Most recently used """

    def __init__(self):
        """ initialize """
        super().__init__()
        self.cache_data = OrderedDict()
    
    def put(self, key, item):
        """ put method"""
        if key and item:
            if key in self.cache_data:
                self.cache_data.update({key: item})
                self.cache_data.move_to_end(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru = self.cache_data.popitem(last=True)
                print('DISCARD:', mru[0])
            self.cache_data[key] = item

    def get(self, key):
        """ Get method """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
