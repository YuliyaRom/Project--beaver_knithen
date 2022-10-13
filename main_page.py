from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    page_title = 'Beaver_knithen: О нас'
    beaver_knithen_main = "Beaver_knithen"
    beaver_knithen_text = "Вязанные изделия любой сложности из наличия и на заказ"
    return render_template('main_page.html', beaver_text=beaver_knithen_text, title=page_title, beaver_main=beaver_knithen_main)



if __name__ == "__main__":
    app.run(debug=True)