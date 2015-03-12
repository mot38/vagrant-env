from flask import Flask
import pymongo
app = Flask(__name__)

# connecting to the database
conn = pymongo.Connection()
db = conn['example-db']
coll = db['example-collection']

@app.route('/add/<forename>/<surname>')
def add_mongodb_record(forename, surname):
    coll.insert({"surname": surname, "forename": forename})
    return 'OK'

@app.route('/find/<surname>')
def find_mongodb_record(surname):
    res = coll.find({"surname": surname})
    return str(list(res))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
