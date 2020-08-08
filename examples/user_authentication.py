import ssl
import argparse
from pymongo import MongoClient
import urllib.parse
from pprint import pprint


class ConnectionManager:
    def __init__(self, user, password, secure_mode, db="test_database"):
        self.username = urllib.parse.quote_plus(user)
        self.password = urllib.parse.quote_plus(password)
        self.client = self.connect_db(secure_mode=secure_mode)
        self.db = self.client[db]

    def connect_db(self, secure_mode="true", ssl_ca_certs='./ssl/rootCA.pem'):
        if secure_mode is "true":
            print("Secure Connection\n")
            return MongoClient("mongodb://%s:%s@127.0.0.1" % (self.username, self.password), ssl="true",
                               ssl_cert_reqs=ssl.CERT_NONE, ssl_ca_certs=ssl_ca_certs)
        else:
            print("Insecure Connection\n")
            return MongoClient("mongodb://%s:%s@127.0.0.1" % (self.username, self.password))

    def fetch_data(self):
        collection = self.db["posts"]
        doc = collection.find({})

        for record in doc:
            pprint(record)

        count = collection.count_documents({})
        print("\nTotal documents :\t {}".format(count))


def main():
    parser = argparse.ArgumentParser(description='Mongodb database authentication', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--u', metavar='N', type=str,
                        help='Mongo username', required=True)
    parser.add_argument('--p', metavar='N', type=str,
                        help='Mongo password', required=True)
    parser.add_argument('--secureMode', metavar='N', type=str,
                        help='enable/disable secure mode', default='true')

    args = parser.parse_args()

    conMngr = ConnectionManager(user=args.u, password=args.p, secure_mode=args.secureMode)

    conMngr.fetch_data()
    conMngr.client.close()


if __name__ == '__main__':
    main()
