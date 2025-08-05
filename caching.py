from cachetools import TTLCache, cached

# Cache decorator with TTL
my_cache = TTLCache(maxsize=100, ttl=10)

@cached(cache=my_cache)
def expensive_operation(x):
    print(f"Computing for {x}")
    return x * 10

print(expensive_operation(2))  # Computes
print(expensive_operation(2))  # Cached