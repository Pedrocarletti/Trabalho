def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
         "name": todo["name"],
        "completed": todo["completed"]
      
    }

def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]

def admin_serial(adm) -> dict:
    return {
        "id": str(adm["_id"]),
        "name": adm["name"],
        "password": adm["password"]

    }

def list_adm(admin) -> list:
    return [admin_serial(adm) for adm in admin]
