from flask import flask, request, render_template
app = Flask(__name__)

@app.route("/",method=["POST","GET"])
def index():
    return  render_template("index.html")

if __name__ == "__main__":
    app.run()