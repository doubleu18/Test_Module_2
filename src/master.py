import pandas as pd
import datetime
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+mysqlconnector://root:warren18@localhost/titanic?host=localhost?port=3306")

conn = engine.connect()

results = conn.execute("SELECT * from titanic").fetchall()
dfTitanic = pd.DataFrame(results, columns=results[0].keys())
dfTitanicTable = pd.DataFrame(results, columns=results[0].keys())
