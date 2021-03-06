import os
from flask import Flask
from flask import jsonify


app=Flask(__name__)

res={ # response json object
    'ServerStatus' : True
}

wd=os.getcwd()

def line(str):
    reportFile=open("report.txt","a")
    reportFile.write("\nProgramName: "+str)
    reportFile.write("\n-----------------------------------------------------------------------------------------------------------------\n")
    reportFile.close()
    return

@app.route("/")
def index():
    res['name']=None
    res['execstatus']=None
    return jsonify(res)

@app.route("/<string:str>")
def certutil(str):
    if str!="favicon.ico":
        x=os.system("py -2"+wd+"\\red_ttp\\"+str+".py >> report.txt")
        line(str)
        res['name']=str
        if x==0:
            res['execstatus']=True
            return jsonify(res)
        else:
            res['execstatus']=False
            return jsonify(res)
    
if __name__ == "__main__":
    os.system("for /f \"tokens=2 delims=[]\" %a in ('ping -n 1 -4 \"%computername%\"') do @echo %a > ipaddr.txt")
    app.run(debug=True,port=5859,host='0.0.0.0')