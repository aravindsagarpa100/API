import os
from flask import Flask


app=Flask(__name__)

@app.route("/<string:str>")
def certutil(str):
    x=os.system("py D:\\RTA\\red_ttp\\"+str+".py")
    if x==0:
        return "{status: successful,name: "+str+"}"
    else:
        return "{status: failed,name: "+str+"}"
    
if __name__ == "__main__":
    app.run(debug=True,port=80)
    os.system("py D:\\RTA\\pagekite.py")