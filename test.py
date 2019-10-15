# import multiprocessing
from pymongo import MongoClient
# from functools import partial
# from itertools import chain

# # calculation function to be applied to every record in the database with an input
# def findAll(i):
#   #define client inside function
#   client = client = MongoClient('localhost', 27017,maxPoolSize=10000)
#   db = client.crawler
#   collection = db['crawler']
#   print(collection.find())
#   #do the calculation with ith element of collection(collection[i]
#   return True

# # pool object creation
# pool = multiprocessing.Pool(processes=8) #spawn 8 processes
# result = pool.map(findAll, [0,])
# pool.close() 

client = MongoClient()
db = client.crawler
collection = db['crawler']

print("DB Status : {}".format(db.command("serverStatus")))