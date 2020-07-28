import redis

def rate_limit(username, api, max_limit=10, expire_time=60):
	"""
	This function returns true or false. Returns true if the user has not
	exceeded the request limit. Otherwise returns false.

	:param username: username of the user making the api call.
	:param api: api endpoint to which the call is made.
	:param max_limit: limit for the user in calls allowed per minute, default=10.
	:param expire_time: expire time in seconds. Default value is 60 seconds.
	:return: boolean, True or False.
	"""

	cache = redis.StrictRedis(port=6379, host='localhost', db=0)

	# key uniquely identifies the username + api combination
	key = username+"-"+api

	# key does not exist yet or has expired
	if cache.get(key) is None:
		cache.setex(key, expire_time, 1)
		return True
	# if the key already exists
	else:
		# The key has expired by the time we get to else
		if cache.ttl(key) == -2:
			cache.setex(key, expire_time, 1)
			return True
		else:
			val = int(cache.get(key))
			if val >= max_limit:
				return False
			else:
				ttl = cache.ttl(key)
				cache.setex(key, ttl, val+1)
				return True
