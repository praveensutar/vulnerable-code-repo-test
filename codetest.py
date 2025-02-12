import os
from flask import Flask, request
app = Flask(__name__)
#test
# curl -X GET "http://localhost:8000/myurl/touch%20HELLO"
@app.route("/myurl/<something>")
def test_sources_7(something):
    
    os.system(request.remote_addr) 

    return "foo"

if __name__ == "__main__":
	app.run(debug=True) 
