from cachetools import TTLCache
from datetime import datetime, timedelta

cache_data = TTLCache(maxsize=50000, ttl=timedelta(days=2), timer=datetime.now)

data_item1 = "http://example1.com"
data_item2 = "http://example2.com"
data_item3 = "http://example3.com"
data_item4 = "http://example4.com"
data_item5 = "http://example5.com"

#Storing data in cache for no longer than 1 hour
cache_data[hash(data_item1)] = data_item1
cache_data[hash(data_item2)] = data_item2
cache_data[hash(data_item3)] = data_item3
cache_data[hash(data_item4)] = data_item4
cache_data[hash(data_item5)] = data_item5

#Accessing data from cache
item = cache_data.get(hash(data_item2), None)

print("Getting from cache = ", item)
