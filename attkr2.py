import os
from flask import Flask
from flask import jsonify


app=Flask(__name__)

res={}

@app.route("/")
def index():
    res['ServerStatus']=True
    return jsonify(res)

@app.route("/<string:str>")
def certutil(str):
    x=os.system("py .\\red_ttp\\"+str+".py")
    if x==0:
        res['status']=True
        res['name']=str
        return jsonify(res)
    else:
        res['status']=False
        res['name']=str
        return jsonify(res)
    
if __name__ == "__main__":
    app.run(debug=True,port=80)