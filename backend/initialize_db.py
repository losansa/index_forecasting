from backend.app import db
import os


cwd = os.getcwd()

db.drop_all()
db.create_all()

with open(os.path.join(cwd, 'inserts.sql')) as inserts_file:
    for insert in inserts_file:
        db.engine.execute(insert)
