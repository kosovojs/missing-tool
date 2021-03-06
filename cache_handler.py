import redis
import json
from config import REDIS_HOST

class CacheHandler:
	redisConn = None
	expireTime = 600#10 min
	prefix = 'WN5jQ4kvYCONVfY07+Bawg4bLxUeFkhK2JrA7fHFa5M='

	def __init__(self):
		self.connect()

	def connect(self):
		self.redisConn = redis.Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True)
	
	def get(self, key):
		data = self.redisConn.get(self.prefix+key)

		if data:
			#print(data, type(data))
			return json.loads(data)
		
		return data

	def ttl(self, key):
		data = self.redisConn.ttl(self.prefix+key)

		return data

	def setData(self, key, data, expireTime = None):
		if expireTime == None:
			expireTime = self.expireTime
		self.redisConn.set(self.prefix+key, json.dumps(data))
		self.redisConn.expire(self.prefix+key, expireTime)