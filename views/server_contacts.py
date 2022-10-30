from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def contacts():
    return render_template("index_contacts.html")

if __name__=="__main__":
    app.run(debug=True)