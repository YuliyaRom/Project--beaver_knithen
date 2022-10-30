from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import csv

import os
import os.path as op

from flask_admin import form
from flask_admin import Admin
from sqlalchemy.event import listens_for

# функция открывает главную страницу
app = Flask(__name__)



@app.route('/')
def main_page():
    title = 'Beaver_knithen: главная страница'
    beaver_text = "Beaver_knithen"
    beaver_description="Вязанные изделия любой сложности из наличия и на заказ"
    return render_template('main.html', title=title, beaver_text=beaver_text, beaver_description=beaver_description)

# создаем базу данных
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# инициализируем админку
admin = Admin(app, name='Beaver_knithen', template_mode='bootstrap3')

class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    description = db.Column(db.String)
    size = db.Column(db.Integer)
    color = db.Column(db.String)
    structure = db.Column(db.String)
    price = db.Column(db.Integer)
    images = db.Column(db.String)

#  функция для удаления продукта
@listens_for(Product, 'after_delete')
def del_image(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(settings.MEDIA_DIR, target.path))
        except OSError:
            pass

        try:
            os.remove(op.join(settings.MEDIA_DIR, form.thumbgen_filename(target.path)))
        except OSError:
            pass
# создаем функцию,которая считает данные из файла и положит в базу

def read_csv(filename):
    print("read_csv")
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['name', 'category', 'description', 'size',
                  'color', 'structure', 'price', 'images']
        reader = csv.DictReader(f, fields, delimiter=';')
        for row in reader:
            save_product(row)
# создаем функцию,которая считает данные построчно
def save_product(row):
    print("save_product")
    product = Product(name=row['name'], category=row['category'],
            description=row['description'],
            size=row['size'], color=row['color'],
            structure=row['structure'],
            price=row['price'], images=row['images'])
    db.session.add(product)
    db.session.commit()

if __name__ == '__main__':
    read_csv('catalog.csv')

# запрос из базы данных
products = db.session.execute(db.select(Product)).scalar()
print(products)
# функция обновляет главную страницу
if __name__ == "__main__":
    app.run(debug=True)