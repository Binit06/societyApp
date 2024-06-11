from flask import Flask, render_template, request, jsonify
from models import db
from sql_query import SQLQuery
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://binit:LsDfhsi11vlO7C0pgNADvUxoCdcz935R@dpg-cpjtebicn0vc73asauo0-a.oregon-postgres.render.com/societyapp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
instance = SQLQuery(db)

@app.route("/")
def home():
    result = db.session.execute(text("SELECT * FROM users"))
    rows = result.fetchall()
    for row in rows:
        print(row)

    return "Check your console for the results"

@app.route('/charges/edit/<int:id>', methods=['GET', 'POST'])
def editCharge(id):
    if request.method == 'GET':
        data = instance.execute_sql_query(f"SELECT * FROM charges WHERE id = {id}")
        print(data)
        columns = ["id", "initialquery", "conditionalquery", "verificationquery", "chargecost", "name"]
        return render_template('edit.html', charges=data[0], column=columns)
    else:
        return "Work Still in Progress"


@app.route("/charges", methods=['GET'])
def salvador():
    charges = instance.get_all_charges_for_showcase()
    return render_template('index.html', charges=charges)


@app.route("/cost")
def cost():
    cost = instance.get_cost_by_id(1)
    return f"The cost of the charge is {cost}"

if __name__ == "__main__":
    app.run(debug=True)


