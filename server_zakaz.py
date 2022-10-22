from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def zakaz():
    return render_template("index_zakaz.html")

if __name__=="__main__":
    app.run(debug=True)