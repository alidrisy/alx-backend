#!/usr/bin/python3
""" FIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - inherts from BaseCaching
      - constants of your cache system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initiliaze """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                k = list(self.cache_data.keys())[0]
                print("DISCARD: ",k)
                self.cache_data.pop(k)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
