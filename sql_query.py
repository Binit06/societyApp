import psycopg2
import json

class SQLQuery:
    def __init__(self):
        self.db_connection = psycopg2.connect(
                dbname="formula_trial",
                user="bijay",
                password="bijay",
                host="localhost",
                port="5432"
            )
    def execute_sql_query(self, query):
        with self.db_connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            charges = []
            if result:
                columns = [col[0] for col in cursor.description]
                result_array = [{columns[i]: row[i] for i in range(len(columns))} for row in result]
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
        with self.db_connection.cursor() as cursor:
            cursor.execute(f"SELECT initialquery FROM charges WHERE id = {id}")
            result = cursor.fetchone()
            return result
    def get_cost_by_id(self, id):
        cost = 0
        with self.db_connection.cursor() as cursor:
            cursor.execute(f"SELECT chargescost FROM charges WHERE id = {id}")
            result = cursor.fetchone()
            if(result[0] == None):
                print("The cost result was None")
                cursor.execute(f"SELECT initialquery FROM charges WHERE id = {id}")
                result = cursor.fetchone()
                cursor.execute(result[0])
                cost_result = cursor.fetchone()
                if cost_result[0] != None :
                    cost = cost_result[0]
            else:
                print("THe cost result has a value")
                cost = result[0]
        return cost
    
    def get_all_charges_for_showcase(self):
        with self.db_connection.cursor() as cursor:
            cursor.execute("SELECT id, name, initialquery, chargescost FROM charges")
            results = cursor.fetchall()
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
