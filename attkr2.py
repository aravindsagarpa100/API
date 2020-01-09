import os
from flask import Flask
from flask import jsonify


app=Flask(__name__)

res={ # response json object
    'ServerStatus' : True
}

@app.route("/")
def index():
    res['name']=None
    res['execstatus']=None
    return jsonify(res)

@app.route("/<string:str>")
def certutil(str):
    if str!="favicon.ico":
        x=os.system("py .\\red_ttp\\"+str+".py >> report.txt")
        res['name']=str
        if x==0:
            res['execstatus']=True
            return jsonify(res)
        else:
            res['execstatus']=False
            return jsonify(res)
    
if __name__ == "__main__":
    app.run(debug=True,port=80)