import json
from sqlalchemy import text

class SQLQuery:
    def __init__(self, db):
        self.cursor = db.session

    def execute_sql_query(self, query):
        initial = self.cursor.execute(text(query))
        result = initial.fetchall()
        charges = []
        if result:
            result_array = [row for row in result]
            return result_array
        else:
            return None

    def is_executable_query(query):
        executable_query_regex = re.compile(r'\b(SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP)\b', re.IGNORECASE)

        if re.search(executable_query_regex, query):
            return True
        else:
            return False

    def get_initial_query(self, id):
        main = self.cursor.execute(text(f"SELECT initialquery FROM charges WHERE id = {id}"))
        result = main.fetchone()
        return result

    def get_cost_by_id(self, id):
        cost = 0
        main = self.cursor.execute(text(f"SELECT chargescost FROM charges WHERE id = {id}"))
        result = main.fetchone()
        if(result[0] == None):
            print("The cost result was None")
            result1 = self.cursor.execute(text(f"SELECT initialquery FROM charges WHERE id = {id}"))
            result = result1.fetchone()
            result2 = self.cursor.execute(text(result[0]))
            cost_result = result2.fetchone()
            if cost_result[0] != None :
                cost = cost_result[0]
        else:
            print("THe cost result has a value")
            cost = result[0]
        return cost
    
    def get_all_charges_for_showcase(self):
        main = self.cursor.execute(text("SELECT id, name, initialquery, chargescost FROM charges"))
        results = main.fetchall()
        charges = []
        for row in results:
            charge = {
                'id': row[0],
                'name': row[1],
                'initial_query': row[2],
                'charges_cost': self.get_cost_by_id(row[0])
            }
            charges.append(charge)
        return charges


    def greet(self):
        return "Hi This is a greeting from my class"
