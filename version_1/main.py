import re
from datetime import datetime

patients = []
next_id = 1  

def validate_dob(dob):
    try:
        if not re.match(r"^\d{2}-\d{2}-\d{4}$", dob):
            raise ValueError("Invalid date format. Use dd-mm-yyyy.")

        day, month, year = map(int, dob.split('-'))
      
        datetime(year, month, day)

        
        if month == 2:  
            if day > 29 or (day == 29 and not is_leap_year(year)):
                raise ValueError("February has only 28 or 29 days.")
        elif month in {4, 6, 9, 11} and day > 30:  
            raise ValueError(f"Month {month:02d} has only 30 days.")
        return True
    except ValueError as e:
        print(e)
        return False



def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)



def calculate_age(dob):
    day, month, year = map(int, dob.split('-'))
    birth_date = datetime(year, month, day)
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age



def validate_phone(phone):
    if not re.match(r"^\d{3}-\d{3}-\d{4}$", phone):
        print("Invalid phone number format. Use xxx-xxx-xxxx.")
        return False
    return True



def add_patient():
    global next_id
    print("\n--- Add New Patient ---")

    first_name = input("Enter First Name: ").strip()
    last_name = input("Enter Last Name: ").strip()


    while True:
        dob = input("Enter Date of Birth (dd-mm-yyyy): ").strip()
        if validate_dob(dob):
            break

    age = calculate_age(dob)

    hometown = input("Enter Hometown: ").strip()
    house_number = input("Enter House Number: ").strip()


    while True:
        phone = input("Enter Phone Number (xxx-xxx-xxxx): ").strip()
        if validate_phone(phone):
            break

    
    patients.append({
        "id": next_id,
        "first_name": first_name,
        "last_name": last_name,
        "date_of_birth": dob,
        "age": age,
        "hometown": hometown,
        "house_number": house_number,
        "phone": phone
    })
    print(f"Patient {first_name} {last_name} added successfully with ID {next_id}.\n")
    next_id += 1



def get_all_patients():
    print("\n--- All Patients ---")
    if not patients:
        print("No patients found.")
        return

    for patient in patients:
        print_patient(patient)



def search_patient_by_id(patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return None



def update_patient_by_id(patient_id):
    patient = search_patient_by_id(patient_id)
    if not patient:
        print("Patient not found.")
        return

    print("\n--- Update Patient ---")
    print_patient(patient)
    print("Leave fields blank to keep existing values.")

    patient["first_name"] = input(f"First Name [{patient['first_name']}]: ").strip() or patient["first_name"]
    patient["last_name"] = input(f"Last Name [{patient['last_name']}]: ").strip() or patient["last_name"]

    while True:
        dob = input(f"Date of Birth (dd-mm-yyyy) [{patient['date_of_birth']}]: ").strip()
        if not dob:
            break
        if validate_dob(dob):
            patient["date_of_birth"] = dob
            patient["age"] = calculate_age(dob)
            break

    patient["hometown"] = input(f"Hometown [{patient['hometown']}]: ").strip() or patient["hometown"]
    patient["house_number"] = input(f"House Number [{patient['house_number']}]: ").strip() or patient["house_number"]

    while True:
        phone = input(f"Phone Number [{patient['phone']}]: ").strip()
        if not phone:
            break
        if validate_phone(phone):
            patient["phone"] = phone
            break

    print("Patient updated successfully.\n")



def delete_patient_by_id(patient_id):
    global patients
    patient = search_patient_by_id(patient_id)
    if not patient:
        print("Patient not found.")
        return

    patients = [p for p in patients if p["id"] != patient_id]
    print(f"Patient with ID {patient_id} deleted successfully.\n")



def print_patient(patient):
    print(f"ID: {patient['id']}")
    print(f"Name: {patient['first_name']} {patient['last_name']}")
    print(f"Date of Birth: {patient['date_of_birth']} (Age: {patient['age']})")
    print(f"Hometown: {patient['hometown']}")
    print(f"House Number: {patient['house_number']}")
    print(f"Phone: {patient['phone']}")
    print("-" * 30)



def main():
    while True:
        print("\n--- Patient Management System ---")
        print("1. Add New Patient")
        print("2. Get All Patients")
        print("3. Search Patient by ID")
        print("4. Update Patient by ID")
        print("5. Delete Patient by ID")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_patient()
        elif choice == "2":
            get_all_patients()
        elif choice == "3":
            try:
                patient_id = int(input("Enter Patient ID: "))
                patient = search_patient_by_id(patient_id)
                if patient:
                    print_patient(patient)
                else:
                    print("Patient not found.")
            except ValueError:
                print("Invalid ID.")
        elif choice == "4":
            try:
                patient_id = int(input("Enter Patient ID: "))
                update_patient_by_id(patient_id)
            except ValueError:
                print("Invalid ID.")
        elif choice == "5":
            try:
                patient_id = int(input("Enter Patient ID: "))
                delete_patient_by_id(patient_id)
            except ValueError:
                print("Invalid ID.")
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

