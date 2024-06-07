from flask import Flask, render_template, request, jsonify
from sql_query import SQLQuery

app = Flask(__name__)
instance = SQLQuery()

@app.route("/")
def home():
    return "This is the home page"

@app.route('/charges/edit/<int:id>', methods=['GET', 'POST'])
def editCharge(id):
    if request.method == 'GET':
        data = instance.execute_sql_query(f"SELECT * FROM charges WHERE id = {id}")
        print(data)
        return render_template('edit.html', charges=data[0])
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


