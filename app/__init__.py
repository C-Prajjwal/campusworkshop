"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi815m4dadc9vm2o4m0-a.oregon-postgres.render.com",
        database="todo_q52y",
        user="todo_q52y_user",
        password="jPaezRtoYojnWE0NjK6TUA4MiXdVGjIk")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
