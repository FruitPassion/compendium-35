#!../.venv/bin/python3

import os
from app import create_app
from sqlalchemy import text

if os.path.exists("database.db"):
    os.remove("database.db")
app = create_app("dev")
with app.app_context():
    from model.shared_model import db
    db.create_all()
    # get all file in sql folder
    sql_list = []
    for root, dirs, files in os.walk('./sql'):
        for file in files:
            if file.endswith(".sql"):
                sql_list.append(os.path.join(root, file))

    for sql in sql_list:
        with open(sql, 'r') as file:
            sql_data = file.read().replace('\n', '')
            sql_data = sql_data.split('##')
        
        with db.engine.connect() as conn:
            for data in sql_data:
                conn.execute(text(data))
            conn.execute(text("COMMIT;"))
