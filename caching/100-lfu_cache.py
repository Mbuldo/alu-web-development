#!/usr/bin/env python3
""" LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
   """ LFUCache defines:
       - caching system with LFU algorithm
       - max number of items from parent BaseCaching
   """

   def __init__(self):
       """ Initialize cache
           Call parent class constructor
       """
       super().__init__()
       self.usage_count = {}
       self.lru_order = []

   def put(self, key, item):
       """ Add an item in the cache using LFU algorithm
       Args:
           key: key to add to cache
           item: value to associate with key
       """
       if key is not None and item is not None:
           if (len(self.cache_data) >= self.MAX_ITEMS and
                   key not in self.cache_data):
               min_freq = min(self.usage_count.values())
               lfu_keys = [k for k, v in self.usage_count.items()
                          if v == min_freq]
               
               if len(lfu_keys) > 1:
                   for lru_key in self.lru_order:
                       if lru_key in lfu_keys:
                           discard_key = lru_key
                           break
               else:
                   discard_key = lfu_keys[0]

               del self.cache_data[discard_key]
               del self.usage_count[discard_key]
               self.lru_order.remove(discard_key)
               print(f"DISCARD: {discard_key}")

           self.cache_data[key] = item
           self.usage_count[key] = self.usage_count.get(key, 0) + 1
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
           self.usage_count[key] += 1
           self.lru_order.remove(key)
           self.lru_order.append(key)
           return self.cache_data[key]
       return None
