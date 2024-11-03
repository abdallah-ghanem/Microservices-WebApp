from flask import Flask,jsonify,render_template
import socket
import sys

app = Flask(__name__)

def fetchDetails():
    hostName = socket.gethostname()  # Provide a default value  
    ip = socket.gethostbyname(hostName)
    return str(hostName),str(ip)

@app.route("/")
def hello_world():
    return "<p>I am DevOps Engineer</p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )


@app.route('/details')
def details(name=None):
    hostName ,ip=fetchDetails()
    return render_template('index.html', person=name,host=hostName,IP=ip)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)