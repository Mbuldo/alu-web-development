#!/usr/bin/env python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines:
      - caching system with FIFO algorithm
      - max number of items from parent BaseCaching
    """

    def __init__(self):
        """ Initialize cache
            Call parent class constructor
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm
        Args:
            key: key to add to cache
            item: value to associate with key
        """
        if key is not None and item is not None:
            if (len(self.cache_data) >= self.MAX_ITEMS and
                    key not in self.cache_data):
                first_key = self.queue.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

            self.cache_data[key] = item
            if key not in self.queue:
                self.queue.append(key)

    def get(self, key):
        """ Get an item by key
        Args:
            key: key to look for in cache
        Returns:
            value associated with key if found, None otherwise
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
