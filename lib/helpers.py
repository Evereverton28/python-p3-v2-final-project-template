from models import get_db_connection

def list_patients():
    conn = get_db_connection()
    patients = conn.execute('SELECT * FROM patients').fetchall()
    conn.close()

    if patients:
        headers = ["ID", "Name", "Age", "Gender", "Medical History"]
        table_width = [len(header) for header in headers]

        for patient in patients:
            table_width[0] = max(table_width[0], len(str(patient['id'])))
            table_width[1] = max(table_width[1], len(patient['name']))
            table_width[2] = max(table_width[2], len(str(patient['age'])))
            table_width[3] = max(table_width[3], len(patient['gender']))
            table_width[4] = max(table_width[4], len(patient['medical_history']))

        header_row = "| " + " | ".join(f"{header:<{table_width[i]}}" for i, header in enumerate(headers)) + " |"
        print("-" * len(header_row))
        print(header_row)
        print("-" * len(header_row))

        for patient in patients:
            row = "| " + " | ".join(f"{str(patient[field]):<{table_width[i]}}" for i, field in enumerate(['id', 'name', 'age', 'gender', 'medical_history'])) + " |"
            print(row)

        print("-" * len(header_row))
    else:
        print("No patients found.")




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

def update_patient():
    patient_id = input("Enter patient ID to update: ")
    name = input("Enter new name: ")
    age = input("Enter new age: ")
    gender = input("Enter new gender: ")
    medical_history = input("Enter new medical history: ")

    conn = get_db_connection()
    conn.execute('UPDATE patients SET name = ?, age = ?, gender = ?, medical_history = ? WHERE id = ?',
                 (name, age, gender, medical_history, patient_id))
    conn.commit()
    conn.close()
    print(f"Patient {patient_id} updated successfully.")

def delete_patient():
    patient_id = input("Enter patient ID to delete: ")

    conn = get_db_connection()
    conn.execute('DELETE FROM patients WHERE id = ?', (patient_id,))
    conn.commit()
    conn.close()
    print(f"Patient {patient_id} deleted successfully.")

def list_doctors():
    conn = get_db_connection()
    doctors = conn.execute('SELECT * FROM doctors').fetchall()
    conn.close()

    if doctors:
        headers = ["ID", "Name", "Specialization"]
        table_width = [len(header) for header in headers]

        for doctor in doctors:
            table_width[0] = max(table_width[0], len(str(doctor['id'])))
            table_width[1] = max(table_width[1], len(doctor['name']))
            table_width[2] = max(table_width[2], len(doctor['specialization']))

        header_row = "| " + " | ".join(f"{header:<{table_width[i]}}" for i, header in enumerate(headers)) + " |"
        print("-" * len(header_row))
        print(header_row)
        print("-" * len(header_row))

        for doctor in doctors:
            row = "| " + " | ".join(f"{str(doctor[field]):<{table_width[i]}}" for i, field in enumerate(['id', 'name', 'specialization'])) + " |"
            print(row)
        
        print("-" * len(header_row))
    else:
        print("No doctors found.")
def add_doctor():
    name = input("Enter name: ")
    specialization = input("Enter specialization: ")
    
    conn = get_db_connection()
    conn.execute('INSERT INTO doctors (name, specialization) VALUES (?, ?)',
                 (name, specialization))
    conn.commit()
    conn.close()
    print(f"Doctor {name} added successfully.")

def update_doctor():
    doctor_id = input("Enter doctor ID to update: ")
    name = input("Enter new name: ")
    specialization = input("Enter new specialization: ")

    conn = get_db_connection()
    conn.execute('UPDATE doctors SET name = ?, specialization = ? WHERE id = ?',
                 (name, specialization, doctor_id))
    conn.commit()
    conn.close()
    print(f"Doctor {doctor_id} updated successfully.")

def delete_doctor():
    doctor_id = input("Enter doctor ID to delete: ")

    conn = get_db_connection()
    conn.execute('DELETE FROM doctors WHERE id = ?', (doctor_id,))
    conn.commit()
    conn.close()
    print(f"Doctor {doctor_id} deleted successfully.")

def list_conditions():
    conn = get_db_connection()
    conditions = conn.execute('SELECT * FROM conditions').fetchall()
    conn.close()

    if conditions:
        headers = ["ID", "Name", "Patient ID", "Doctor ID"]
        table_width = [len(header) for header in headers]

        for condition in conditions:
            table_width[0] = max(table_width[0], len(str(condition['id'])))
            table_width[1] = max(table_width[1], len(condition['name']))
            table_width[2] = max(table_width[2], len(str(condition['patient_id'])))
            table_width[3] = max(table_width[3], len(str(condition['doctor_id'])))

        header_row = "| " + " | ".join(f"{header:<{table_width[i]}}" for i, header in enumerate(headers)) + " |"
        print("-" * len(header_row))
        print(header_row)
        print("-" * len(header_row))

        for condition in conditions:
            row = "| " + " | ".join(f"{str(condition[field]):<{table_width[i]}}" for i, field in enumerate(['id', 'name', 'patient_id', 'doctor_id'])) + " |"
            print(row)

        print("-" * len(header_row))
    else:
        print("No conditions found.")


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
    
def delete_condition():
    condition_id = input("Enter the ID of the condition to delete: ")
    conn = get_db_connection()
    conn.execute('DELETE FROM conditions WHERE id = ?', (condition_id,))
    conn.commit()
    conn.close()
    print("Condition deleted successfully.")

def list_symptoms():
    conn = get_db_connection()
    symptoms = conn.execute('SELECT * FROM symptoms').fetchall()
    conn.close()

    if symptoms:
        headers = ["ID", "Name", "Condition ID"]
        table_width = [len(header) for header in headers]

        for symptom in symptoms:
            table_width[0] = max(table_width[0], len(str(symptom['id'])))
            table_width[1] = max(table_width[1], len(symptom['name']))
            table_width[2] = max(table_width[2], len(str(symptom['condition_id'])))

        header_row = "| " + " | ".join(f"{header:<{table_width[i]}}" for i, header in enumerate(headers)) + " |"
        print("-" * len(header_row))
        print(header_row)
        print("-" * len(header_row))

        for symptom in symptoms:
            row = "| " + " | ".join(f"{str(symptom[field]):<{table_width[i]}}" for i, field in enumerate(['id', 'name', 'condition_id'])) + " |"
            print(row)

        print("-" * len(header_row))
    else:
        print("No symptoms found.")


def add_symptom():
    name = input("Enter symptom name: ")
    condition_id = input("Enter condition ID: ")
    
    conn = get_db_connection()
    conn.execute('INSERT INTO symptoms (name, condition_id) VALUES (?, ?)',
                 (name, condition_id))
    conn.commit()
    conn.close()
    print(f"Symptom {name} added successfully.")

def delete_symptom():
    symptom_id = input("Enter the ID of the symptom to delete: ")
    conn = get_db_connection()
    conn.execute('DELETE FROM symptoms WHERE id = ?', (symptom_id,))
    conn.commit()
    conn.close()
    print("Symptom deleted successfully.")

def exit_program():
    print("Exiting the program...")
    exit()
