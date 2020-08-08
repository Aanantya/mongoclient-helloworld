from pymongo import MongoClient
import datetime
import pprint
import argparse
import json
import ssl

isTrue = lambda val: True if val.lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh',
                                             'on'] else False


class TestData:
    post = {"author": "Ram",
            "text": "My second blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}


class MongoDBMgr:

    def __init__(self, secure_mode, ip='127.0.0.1', port=27017, db='test_database'):
        self.client = self.__connect_db(ip=ip, port=port, secure_mode=secure_mode)
        self.db = self.client[db]
        self.post_id = None

    def __connect_db(self, ip='127.0.0.1', port=27017, secure_mode="true", ssl_ca_certs='./ssl/rootCA.pem'):
        if secure_mode == "true":
            return MongoClient(ip, port, ssl=secure_mode, ssl_cert_reqs=ssl.CERT_NONE, ssl_ca_certs=ssl_ca_certs)
        else:
            return MongoClient(ip, port)

    def insert_test_data(self, post=TestData.post):
        db = self.db
        posts = db.posts
        self.post_id = post_id = posts.insert_one(post).inserted_id
        print("Store it for query. post ID is {} ".format(post_id))

    def find_all(self):
        db = self.db
        posts = db.posts
        doc = posts.find({})

        for record in doc:
            print("\n")
            pprint.pprint(record)

        count = posts.count_documents({})
        print("\n Current number of entries are : {}".format(count))
        return

    def close(self):
        self.client.close()
        return


def main():
    parser = argparse.ArgumentParser(description='Mongodb hello world',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--ip', metavar='N', type=str,
                        help='Mongo server IP', default='localhost')
    parser.add_argument('--port', metavar='N', type=int,
                        help='Mongo server Port', default=27017)
    parser.add_argument('--secureMode', metavar='N', type=str,
                        help='enable/disable secure mode', default='true')
    parser.add_argument('--post', metavar='N', type=str,
                        help='Post test data', default='false')
    parser.add_argument('--postdata', metavar='N', type=str,
                        help='Post Data value', default=None)
    parser.add_argument('--fetch', metavar='N', type=str,
                        help='Fetch all data', default='yes')
    args = parser.parse_args()

    mongoDBMgr = MongoDBMgr(ip=args.ip, port=args.port, secure_mode=args.secureMode)
    postdata = None

    try:
        if args.postdata:
            postdata = json.loads(args.postdata)
            postdata['date'] = datetime.datetime.utcnow()
        elif isTrue(args.post.lower()):
            postdata = TestData.post
        if postdata:
            print("Inserting a test data")
            mongoDBMgr.insert_test_data(post=postdata)
        if isTrue(args.fetch.lower()):
            print("Fetching test data")
            mongoDBMgr.find_all()

    except:
        print("Something went wrong")

    finally:
        mongoDBMgr.close()


if __name__ == "__main__":
    main()
