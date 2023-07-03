from src.contract import db_connection as db

print(db.read_setting('test_setting'))
