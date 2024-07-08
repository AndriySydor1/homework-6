import sqlite3

def execute_query(query_file, params=None):
    conn = sqlite3.connect('data/university.db')
    cursor = conn.cursor()

    with open(query_file, 'r') as file:
        query = file.read()

    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
        
    results = cursor.fetchall()
    for row in results:
        print(row)

    conn.close()

if __name__ == "__main__":
    # Приклад виконання запиту з параметрами
    execute_query('queries/query_1.sql')
    execute_query('queries/query_2.sql', (1,))
    