import pdb
from pymongo import MongoClient
import datetime
import pprint
import argparse
isTrue = lambda  val : True if val.lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh', 'on'] else False

class MongoDBMgr:
    def __init__(self, ip='127.0.0.1', port=27017, db='test_database'):
      self.client = self.__connect_db(ip, port)
      self.db = self.client[db]
      self.post_id = None
  
    def __connect_db(self, ip='127.0.0.1', port=27017):
        return MongoClient(ip, port)
        

    def insert_test_data(self):
        db = self.db
        post = {"author": "Mike4",
                 "text": "My first blog post!",
                 "tags": ["mongodb", "python", "pymongo"],
                 "date": datetime.datetime.utcnow()}
        posts = db.posts
        self.post_id= post_id = posts.insert_one(post).inserted_id
        print("Store it for query. post ID is {} ".format(post_id))

    def find_one(self):
        post_id = self.post_id         
        db = self.db
        posts = db.posts
        if post_id:
            query = {"_id": post_id}
            pprint.pprint(posts.find_one(query))
        else:
            pprint.pprint(posts.find_one())
        count = posts.count_documents({})
        print("Current number of entries are {}".format(count))
        return
	

def main():
    parser = argparse.ArgumentParser(description='Mongodb hello world', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
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
    if isTrue(args.add.lower()):
        print("Inserting a test data")
        mongoDBMgr.insert_test_data()
    if isTrue(args.fetch.lower()):
        print("Fetching test data")
        mongoDBMgr.find_one()

if __name__ == "__main__":
    main()
