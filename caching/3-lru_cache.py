#!/usr/bin/env python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines:
        - caching system with LRU algorithm
        - max number of items from parent BaseCaching
    """

    def __init__(self):
        """ Initialize cache
            Call parent class constructor
        """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """ Add an item in the cache using LRU algorithm
        Args:
            key: key to add to cache
            item: value to associate with key
        """
        if key is not None and item is not None:
            if (len(self.cache_data) >= self.MAX_ITEMS and
                    key not in self.cache_data):
                lru_key = self.lru_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            if key in self.lru_order:
                self.lru_order.remove(key)
            self.lru_order.append(key)

    def get(self, key):
        """ Get an item by key
        Args:
            key: key to look for in cache
        Returns:
            value associated with key if found, None otherwise
        """
        if key is not None and key in self.cache_data:
            self.lru_order.remove(key)
            self.lru_order.append(key)
            return self.cache_data[key]
        return None
