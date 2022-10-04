from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def about_us():
    page_title = 'Beaver_knithen: О нас'
    beaver_knithen_text = "Компания Beaver_knithen представляет"
    return render_template('about_us.html', beaver_text=beaver_knithen_text, title=page_title)



if __name__ == "__main__":
    app.run(debug=True)