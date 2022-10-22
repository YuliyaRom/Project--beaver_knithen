from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    title = 'Beaver_knithen: главная страница'
    beaver_text = "Beaver_knithen"
    beaver_description="Вязанные изделия любой сложности из наличия и на заказ"
    return render_template('main.html', title=title, beaver_text=beaver_text, beaver_description=beaver_description)



if __name__ == "__main__":
    app.run(debug=True)