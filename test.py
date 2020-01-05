import common
import os
from flask import Flask

app=Flask(__name__)

@app.route("/certutil")
def cert():
    common.log("Encoding target")
    encoded_file = os.path.abspath('encoded.txt')
    decoded_file = os.path.abspath('decoded.exe')
    common.execute("c:\\Windows\\System32\\certutil.exe -encode c:\\windows\\system32\\cmd.exe \"%s\"" % encoded_file)

    common.log("Decoding target")
    common.execute("c:\\Windows\\System32\\certutil.exe -decode \"%s\" \"%s\"" % (encoded_file, decoded_file))

    common.log("Cleaning up")
    common.remove_file(encoded_file)
    common.remove_file(decoded_file)
    return "{status: succesful}"


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
