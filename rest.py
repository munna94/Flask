from flask import Flask, request
from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client.flaskTest

app = Flask(__name__)

#---hit using http://127.0.0.1:2020/rest/api/?name=mk&salary=1000k--------

@app.route('/rest/api/', methods=['GET'])
def foo():   
    bar = request.args.to_dict()
    keys=bar.keys()
    dd={'name':bar[str(keys[0])],'salary':bar[str(keys[1])]}
    db.testCollection.insert_one(dd)
    return "success"

#-----hit http://127.0.0.1:2020/getdata/10 ---it will return welcome 10--
@app.route('/getdata/<name>')
def success(name):
    return 'welcome %s' % name

if __name__ == '__main__':   
    app.run(port=2020)	
	

