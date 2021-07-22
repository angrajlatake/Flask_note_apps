# from enum import unique
# from flask import Flask, render_template,redirect,request
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)

# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, unique=True, nullable=False)
#     password = db.Column(db.String, unique=True, nullable=False)

#     def __repr__(self) -> str:
#         return f"{self.username}"

from website import create_app

app = create_app()

if __name__ =="__main__":
    app.run(debug=True)
