from . import get_db_connection

def list_symptoms():
    conn = get_db_connection()
    symptoms = conn.execute('SELECT * FROM symptoms').fetchall()
    for symptom in symptoms:
        print(dict(symptom))
    conn.close()

def add_symptom():
    name = input("Enter symptom name: ")
    condition_id = input("Enter condition ID: ")
    
    conn = get_db_connection()
    conn.execute('INSERT INTO symptoms (name, condition_id) VALUES (?, ?)',
                 (name, condition_id))
    conn.commit()
    conn.close()
    print(f"Symptom {name} added successfully.")
