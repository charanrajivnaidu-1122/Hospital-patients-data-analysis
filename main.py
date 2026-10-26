from modules.visualizations import (
    show_age_distribution,
    show_gender_distribution,
    show_city_distribution
)

from modules.patient_management import (
    add_patient,
    view_patients,
    search_patient,
    update_patient_age,
    delete_patient
)

from modules.data_analysis import analyze_patients


print("\n===== HOSPITAL PATIENT DATA ANALYSIS SYSTEM =====")

print("1. View all patients")
print("2. Add patient")
print("3. Search patient")
print("4. Update patient age")
print("5. Delete patient")
print("6. Analyze patient data")
print("7. Show age distribution graph")
print("8. Show gender distribution graph")
print("9. Show city distribution graph")

choice = input("Enter your choice: ")

if choice == "1":
    view_patients()

elif choice == "2":
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    city = input("Enter city: ")

    add_patient(name, age, gender, city)

elif choice == "3":
    patient_id = int(input("Enter patient ID: "))
    search_patient(patient_id)

elif choice == "4":
    patient_id = int(input("Enter patient ID: "))
    new_age = int(input("Enter new age: "))

    update_patient_age(patient_id, new_age)

elif choice == "5":
    patient_id = int(input("Enter patient ID: "))
    delete_patient(patient_id)

elif choice == "6":
    analyze_patients()

elif choice == "7":
    show_age_distribution()

elif choice == "8":
    show_gender_distribution()

elif choice == "9":
    show_city_distribution()

else:
    print("Invalid choice.")
