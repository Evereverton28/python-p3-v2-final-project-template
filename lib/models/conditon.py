from . import get_db_connection

def list_conditions():
    conn = get_db_connection()
    conditions = conn.execute('SELECT * FROM conditions').fetchall()
    for condition in conditions:
        print(dict(condition))
    conn.close()

def add_condition():
    name = input("Enter condition name: ")
    patient_id = input("Enter patient ID: ")
    doctor_id = input("Enter doctor ID: ")
    
    conn = get_db_connection()
    conn.execute('INSERT INTO conditions (name, patient_id, doctor_id) VALUES (?, ?, ?)',
                 (name, patient_id, doctor_id))
    conn.commit()
    conn.close()
    print(f"Condition {name} added successfully.")
