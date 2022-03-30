from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id':1,
        'contact':'65742897',
        'name':'english man',
        'done':False
    },
    {
        'id':2,
        'contact':'67432198',
        'name':'indian man',
        'done':False
    }
]

@app.route("/")
def hw():
    return "O RUPEES IN ACCOUNT"

@app.route("/add-data",methods=["POST"])
def ad():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"PLEASE PROVIDE DATA"
        },404)
    task = {
        'id':tasks[0]['id']+1,
        'contact':request.json['contact'],
        'name':request.json.get['name',""],
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "status":"succesess",
        "message":"DATA ADDED!"
    })

@app.route("/get-data")
def gt():
    return jsonify({
        "data":tasks
    })

if (__name__ == '__main__'):
    app.run(debug = True)