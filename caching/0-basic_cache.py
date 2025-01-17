#!/usr/bin/env python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
        - caching system without limit
        - inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize the cache
            Call parent class constructor
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        Args:
            key: key to add in cache
            item: value to associate with key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

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
