# mongodb-helloworld
hello world code for mongodb 

# How to test

* Install pymongo in your machine (preferrably python virtual env which helps to keep setup not interfered with others)
* Run python3 mongoclient.py --help

# Example

## Simple
python3 mongoclient.py --ip 154.3.80.114

## Advanced
In this example, I will add a custom entry using a file

**(envmongo)$ cat data.txt**

{"author": "Hello", "text": "My first blog post!","tags": ["mongodb", "python", "pymongo"]}

**(envmongo) Deepaks-MacBook-Air:mongodb-helloworld deepak$ ls**

README.md	data.txt	mongoclient.py

**(envmongo)$ python3 mongoclient.py --ip test.com --postdata  "$(cat data.txt)"**

Inserting a test data

Store it for query. post ID is 5ed0f56654881235f1de305f 

Fetching test data

{'_id': ObjectId('5ed0f56654881235f1de305f'),
 'author': 'Hello',
 'date': datetime.datetime(2020, 5, 29, 11, 43, 34, 9000),
 'tags': ['mongodb', 'python', 'pymongo'],
 'text': 'My first blog post!'}
 
Current number of entries are 18


# Reference

https://api.mongodb.com/python/current/tutorial.html
