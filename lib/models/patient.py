from . import get_db_connection

def list_patients():
    conn = get_db_connection()
    patients = conn.execute('SELECT * FROM patients').fetchall()
    for patient in patients:
        print(dict(patient))
    conn.close()

def add_patient():
    name = input("Enter name: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    medical_history = input("Enter medical history: ")
    
    conn = get_db_connection()
    conn.execute('INSERT INTO patients (name, age, gender, medical_history) VALUES (?, ?, ?, ?)',
                 (name, age, gender, medical_history))
    conn.commit()
    conn.close()
    print(f"Patient {name} added successfully.")
