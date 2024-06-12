# lib/cli.py

from helpers import (
    exit_program,
    list_patients,
    add_patient,
    update_patient,
    delete_patient,
    list_doctors,
    add_doctor,
    update_doctor,
    delete_doctor,
    list_conditions,
    add_condition,
    delete_condition,
    list_symptoms,
    add_symptom,
    delete_symptom
)

from models import initialize_db

def main():
    initialize_db()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_patient()
        elif choice == "2":
            list_patients()
        elif choice == "3":
            update_patient()
        elif choice == "4":
            delete_patient()
        elif choice == "5":
            add_doctor()
        elif choice == "6":
            list_doctors()
        elif choice == "7":
            update_doctor()
        elif choice == "8":
            delete_doctor()
        elif choice == "9":
            add_symptom()
        elif choice == "10":
            list_symptoms()
        elif choice == "11":
            delete_symptom()
        elif choice == "12":
            add_condition()
        elif choice == "13":
            list_conditions()
        elif choice == "14":
            delete_condition()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a patient")
    print("2. List all patients")
    print("3. Update a patient")
    print("4. Delete a patient")
    print("5. Add a doctor")
    print("6. List all doctors")
    print("7. Update a doctor")
    print("8. Delete a doctor")
    print("9. Add a symptom")
    print("10. List all symptoms")
    print("11. Delete a symptom")
    print("12. Add a condition")
    print("13. List all conditions")
    print("14. Delete a condition")


if __name__ == "__main__":
    main()
