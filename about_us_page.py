from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def about_us():
    page_title = 'Beaver_knithen: О нас'
    beaver_knithen_about_us = "Компания Beaver_knithen представляет"
    return render_template('about_us.html', title=page_title, beaver_about=beaver_knithen_about_us)



if __name__ == "__main__":
    app.run(debug=True)