#!/usr/bin/env python3
""" MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
   """MRUCache defines:
   - caching system with MRU algorithm
   - max number of items from parent BaseCaching
   """

   def __init__(self):
       """Initialize cache
       Call parent class constructor
       """
       super().__init__()
       self.mru_order = []

   def put(self, key, item):
       """Add an item in the cache using MRU algorithm
       Args:
           key: key to add to cache
           item: value to associate with key
       """
       if key is not None and item is not None:
           if (len(self.cache_data) >= self.MAX_ITEMS and
                   key not in self.cache_data):
               mru_key = self.mru_order.pop()
               del self.cache_data[mru_key]
               print(f"DISCARD: {mru_key}")

           self.cache_data[key] = item
           if key in self.mru_order:
               self.mru_order.remove(key)
           self.mru_order.append(key)

   def get(self, key):
       """Get an item by key
       Args:
           key: key to look for in cache
       Returns:
           value associated with key if found, None otherwise
       """
       if key is not None and key in self.cache_data:
           self.mru_order.remove(key)
           self.mru_order.append(key)
           return self.cache_data[key]
       return None
