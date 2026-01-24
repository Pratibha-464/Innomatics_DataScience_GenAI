from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/<user_name>")
def convert(user_name):
    user_name =  request.args.get("user_name")

    if user_name == user_name.upper():
        status = "already"
        result = user_name
    else:
        status = "converted"
        result = user_name.upper()  
       
    return render_template("thankyou.html", result = result, status = status)

if __name__ == '__main__':
    app.run(debug=True)
