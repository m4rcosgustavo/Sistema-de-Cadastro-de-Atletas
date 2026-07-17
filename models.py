from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)


class Esporte(db.Model):
    __tablename__ = "esportes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    atletas = db.relationship(
        "Atleta",
        backref="esporte",
        lazy=True
    )


class Atleta(db.Model):
    __tablename__ = "atletas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)

    esporte_id = db.Column(
        db.Integer,
        db.ForeignKey("esportes.id"),
        nullable=False
    )