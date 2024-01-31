#!/usr/bin/python3
""" LRUCache module
"""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines:
      - inherts from BaseCaching
      - constants of your cache system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.lru_data = {}

    def __pop(self, key):
        """privet method to discard the least recently used item """
        k = ''
        i = 0
        for ke, val in self.lru_data.items():
            if i == 0:
                k = ke
            if self.lru_data[k] > val:
                k = ke
            i += 1
        print("DISCARD:", k)
        self.lru_data.pop(k)
        self.cache_data.pop(k)

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.__pop(key)
        self.lru_data[key] = datetime.now()

    def get(self, key):
        """ Get an item by key
        """
        if key in self.lru_data.keys():
            self.lru_data[key] = datetime.now()
        return self.cache_data.get(key)
