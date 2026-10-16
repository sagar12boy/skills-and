from flask import Flask,jsonify,request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sagar",
    database = "student"
)
@app.route("/employes/",methods = ["GET"])
def home(employee_id):
    cursor = db.cursor()
    cursor.execute("select * from employes")
    data = cursor.fetchall()
students = []
    for row in data:
        students.append({
            "id": row[0],
            "name": row[1],
            "city": row[2],
            "gender": row[3],
            "purchase": row[4]
        })
return jsonify({
    "success": True,
    "message": "students updated successfully",
    "data": students
})
 
if __name__ == "__main__":
    app.run(debug=True)

    



