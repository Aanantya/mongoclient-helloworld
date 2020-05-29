import pdb
from pymongo import MongoClient
import datetime
import pprint
import argparse

class MongoDBMgr:
    def __init__(self, ip='127.0.0.1', port=27017, db='test_database'):
      self.client = self.__connect_db(ip, port)
      self.db = self.client[db]
  
    def __connect_db(self, ip='127.0.0.1', port=27017):
        return MongoClient(ip, port)
        

    def insert_test_data(self):
        db = self.db
        post = {"author": "Mike",
                 "text": "My first blog post!",
                 "tags": ["mongodb", "python", "pymongo"],
                 "date": datetime.datetime.utcnow()}
        posts = db.posts
        post_id = posts.insert_one(post).inserted_id

    def find_one(self):
       db = self.db
       posts = db.posts
       pprint.pprint(posts.find_one())
       return
	

def main():
    parser = argparse.ArgumentParser(description='Mongodb hello world')
    parser.add_argument('--ip', metavar='N', type=str,
                           help='Mongo server IP', default='localhost')
    parser.add_argument('--port', metavar='N', type=int,
                           help='Mongo server Port', default=27017)
    parser.add_argument('--add', metavar='N', type=str,
                           help='Insert test data', default='no')
    parser.add_argument('--fetch', metavar='N', type=str,
                           help='Check test data', default='yes')
    args = parser.parse_args()
    mongoDBMgr = MongoDBMgr(args.ip, args.port)
    if args.add == "yes":
        print("Inserting a test data")
        mongoDBMgr.insert_test_data()
    if args.fetch == "yes":
        print("Fetching test data")
        mongoDBMgr.find_one()

if __name__ == "__main__":
    main()
