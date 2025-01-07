from django.shortcuts import HttpResponse

from django.core.cache import cache

def set_cache_example(request):
    cache.set('my_key', 'Hello, Redis!', timeout=60*15)  # Set cache with a 15-minute timeout
    return HttpResponse("Cache set successfully.")

def get_cache_example(request):
    value = cache.get('my_key')
    return HttpResponse(f"Cache value: {value}")
