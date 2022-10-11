employee = {
    "id":1,
    "name":"Gipsz Jakab"
}

employees = []
employees.append(employee)

repeat = True

while repeat:
    input_id = input("ID: ")
    input_name = input("name")

    employee = {
    "id":input_id,
    "name":input_name
    }
    employees.append(employee)
    print(employees)

    input_exit = input("Szeretnéd-e folytatni?(i/n)")
    if(input_exit.lower()=="n"):
        repeat=False
    

