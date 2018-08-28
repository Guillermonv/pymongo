from flask import Flask
from pymongo import MongoClient
from flask import request, jsonify


client = MongoClient()

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('localhost', 27017)
db = client.local
# Step 2: collection
mycol = db["customers"]


app = Flask(__name__)

@app.route("/post/<name>/<address>")
def add(name,address):
    mydict = {"name": name, "address":address}

    mycol.insert_one(mydict)
    return "Field inserted"


@app.route("/getall")
def getall():
  #  si las direcciones o los nombres son nulos en la base falla
    output = []
    for s in mycol.find():
        output.append({'name': s['name'], 'address' : s['address']})
    return jsonify({'result': output})


@app.route("/get/<name>")
def getbyproperty(name):
    s = mycol.find_one({'name': name})
    if s:
        output = {'name': s['name'], 'address': s['address']}
    else:
        output = "No such name"
    return jsonify({'result': output})

@app.route("/del/<name>")
def delperson(name):
 mycol.delete_one({'name': name})
 return "borrado"



@app.route("/")
def home_page():

    return "home"


@app.route("/name/<name>")
def user_profile(name):
    user = client.db.customers.find_one_or_404({"_id": name})
    return render_template("user.html",
        name=name)



if __name__ == '__main__':
    app.run(debug=True)

