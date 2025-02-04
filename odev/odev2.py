from flask import Flask ,jsonify

app = Flask(__name__)

@app.route('/greet/<name>',methods = ['GET'] )
def get_name(name):
    return jsonify({"message": "Hello, " + name +"! Welcome to the Flask world!"})



@app.route('/greet/',methods = ['GET'] )
def get():
    return jsonify({"message": "Hello! Please provide a name in the URL."})




if __name__ == '__main__':
    app.run(debug=True)

