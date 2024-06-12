from . import get_db_connection

def list_doctors():
    conn = get_db_connection()
    doctors = conn.execute('SELECT * FROM doctors').fetchall()
    for doctor in doctors:
        print(dict(doctor))
    conn.close()

def add_doctor():
    name = input("Enter name: ")
    specialization = input("Enter specialization: ")
    
    conn = get_db_connection()
    conn.execute('INSERT INTO doctors (name, specialization) VALUES (?, ?)',
                 (name, specialization))
    conn.commit()
    conn.close()
    print(f"Doctor {name} added successfully.")
