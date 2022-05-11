from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configure sqlite db to connect to
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# db variable is instance of sqlalchemy, pass in Flask app
db = SQLAlchemy(app)


class Drink(db.Model):
    # attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    # self refers to object, grabs object's attributes with self.___
    def __repr__(self):
        return f"{self.name} - {self.description}"



# (end point)
@app.route('/')
def index():
    return 'Hello!'

# get request, app route to 'get' drinks
@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()

    output = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}

        output.append(drink_data)
    return {'drinks': output}

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {'name': drink.name, 'description': drink.description}
    # if not working with dictionary, use jsonify

@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'],
                description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}

@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "404, not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "ya got it"}


# notes:

    # database (created and interacting w/through terminal): 
        # db.create_all() created data.db
        # as this is an ORM (object relational mapper), work w/relational db w/objects
        # create drink object by assigning to variable, w/name parameter
            # drink = Drink(name='Grape Soda', description='Tastes like grapes')
        # add to database --> db.session.add(drink) , db.session.commit()