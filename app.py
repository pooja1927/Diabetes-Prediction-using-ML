import pickle
from flask import Flask,request,render_template
import sqlite3

app=Flask(__name__)
model=pickle.load(open('diabetes.pkl','rb'))

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/diabetes', methods=['GET','POST'])
def diabetes():
    db = sqlite3.connect('diabetes.db')
    cursor = db.cursor()
    lst = []
    data = request.form.values()
    for val in data:
        if type(val)==str:
            lst.append(val)
        else:
            try:
                val = int(val)
            except:
                val = float(val)
            lst.append(int(val))
    query2 = """INSERT INTO data (Name,Address,Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age) VALUES (?, ?, ?, ?, ?, ?,?, ?, ?, ?);"""
    # print(tuple(lst))
    cursor.execute(query2,tuple(lst))
    db.commit()
    db.close()
    result = model.predict([lst[2:]])
    if result[0]==1:
        return render_template('yes.html')
    else:
        return render_template('no.html')
    # return str(result[0])
if __name__ == '__main__':
    app.run(debug=True)