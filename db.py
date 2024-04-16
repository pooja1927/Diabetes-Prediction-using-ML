import sqlite3

db = sqlite3.connect('diabetes.db')

query ="""CREATE TABLE data (
    Name varchar,
    Address varchar,
    Pregnancies int,
    Glucose int,
    BloodPressure int,
    SkinThickness int,
    Insulin int,
    BMI int,
    DiabetesPedigreeFunction int,
    Age int
);"""

cur = db.cursor()

cur.execute(query)



db.commit()
cur.close()
