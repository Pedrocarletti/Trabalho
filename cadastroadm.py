from pymongo import MongoClient


class AdminCRUD:
    def __init__(self):
        self.client = self.connect_to_db()
        self.db = self.client['pedro']
        self.collection = self.db['admin_collection']

    def connect_to_db(self):
        client = MongoClient("mongodb+srv://pedro:pedro@cluster0.lo2qxc0.mongodb.net/?retryWrites=true&w=majority")
        return client

    def create_admin(self, username, password):
        admin = {'username': username, 'password': password, 'role': 'admin'}
        result = self.collection.insert_one(admin)
        return result.inserted_id

    def read_admin(self, username):
        admin = self.collection.find_one({"username": username})
        return admin

    def update_admin(self, username, new_password):
        result = self.collection.update_one(
            {"username": username},
            {"$set": {"password": new_password}}
        )
        return result.modified_count

    def delete_admin(self, username):
        result = self.collection.delete_one({"username": username})
        return result.deleted_count
