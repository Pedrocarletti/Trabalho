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
        "username": adm["username"],
        "password": adm["password"]

    }

def list_adm(admin) -> list:
    return [admin_serial(adm) for adm in admin]



def filedata_serial(file) -> dict:
    return {
        "id": str(file["_id"]),
        "filename": file["filename"],
       
        "rarity": file["rarity"],
        "name": file["name"],
        "value": file["value"]

    }
def list_filedatas(file_data) -> list:
    return [filedata_serial(file) for file in file_data]
