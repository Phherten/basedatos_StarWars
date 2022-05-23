from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False) #no puede ser nulo este campo
    gender = db.Column(db.String(120), unique=False, nullable=True) #este campopuede ser nulo
    hair_color = db.Column(db.String(120), unique=False, nullable=True) #este también
    

    def __repr__(self):
        return '<People %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False) #no puede ser nulo este campo
    clima = db.Column(db.String(120), unique=False, nullable=True) #este campopuede ser nulo
    tamaño = db.Column(db.Integer, unique=False, nullable=True) #este también
    

    def __repr__(self):
        return '<Planet %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "clima": self.clima,
            "tamaño": self.tamaño,
            # do not serialize the password, its a security breach
        }

class Fav_people(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #quien le dio a favorito
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #quien es el favorito
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    #defino las relaciones
    rel_user = db.relationship(User)
    rel_people = db.relationship(People)

    def __repr__(self):
        return '<FavPeople %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
         
            # do not serialize the password, its a security breach
        }

class Fav_planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #quien le dio a favorito
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #quien es el favorito
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    #defino las relaciones
    rel_user = db.relationship(User)
    rel_planet = db.relationship(Planet)

    def __repr__(self):
        return '<FavPlanet %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
         
            # do not serialize the password, its a security breach
        }
