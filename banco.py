# Path: banco.py

#this function will connect to the database mongodb
def connect():
    try:
        connection = MongoClient('localhost', 27017)
        return connection
    except:
        print("Could not connect to MongoDB")

#this function will insert a new user in the database
def insert_user(user):
    try:
        connection = connect()
        db = connection['users']
        db.users.insert_one(user)
        return user
    except:
        print("Could not insert user")

#this function will find a user in the database
def find_user(user):
    try:
        connection = connect()
        db = connection['users']
        return db.users.find_one(user)
    except:
        print("Could not find user")

#this function will update a user in the database
#param: user: the user to be updated
#return: the user updated
#raise: error if the update fails
def update_user(user):
    try:
        connection = connect()
        db = connection['users']
        db.users.update_one({"_id": user["_id"]}, {"$set": user}, upsert=False)
        return user
    except:
        print("Could not update user")

#this function will delete a user in the database
#param: user: the user to be deleted
#return: the user deleted
#raise: error if the deletion fails
def delete_user(user):
    try:
        connection = connect()
        db = connection['users']
        db.users.delete_one(user)
        return user
    except:
        print("Could not delete user")

#this function will insert a new sale in the database
#param: sale: the sale to be inserted
#return: the sale inserted
#raise: error if the insertion fails
def insert_sale(sale):
    try:
        connection = connect()
        db = connection['sales']
        db.sales.insert_one(sale)
        return sale
    except:
        print("Could not insert sale")

#this function will find a sale in the database
#param: sale: the sale to be found
#return: the sale found
#raise: error if the search fails
def find_sale(sale):
    try:
        connection = connect()
        db = connection['sales']
        return db.sales.find_one(sale)
    except:
        print("Could not find sale")

#this function will update a sale in the database
#param: sale: the sale to be updated
#return: the sale updated
#raise: error if the update fails
def update_sale(sale):
    try:
        connection = connect()
        db = connection['sales']
        db.sales.update_one({"_id": sale["_id"]}, {"$set": sale}, upsert=False)
        return sale
    except:
        print("Could not update sale")

#this function will delete a sale in the database
#param: sale: the sale to be deleted
#return: the sale deleted
#raise: error if the deletion fails
def delete_sale(sale):
    try:
        connection = connect()
        db = connection['sales']
        db.sales.delete_one(sale)
        return sale
    except:
        print("Could not delete sale")

#this function will insert a new product in the database
#param: product: the product to be inserted
#return: the product inserted
#raise: error if the insertion fails
def insert_product(product):
    try:
        connection = connect()
        db = connection['products']
        db.products.insert_one(product)
        return product
    except:
        print("Could not insert product")

#this function will find a product in the database
#param: product: the product to be found
#return: the product found
#raise: error if the search fails
def find_product(product):
    try:
        connection = connect()
        db = connection['products']
        return db.products.find_one(product)
    except:
        print("Could not find product")

#this function will update a product in the database
#param: product: the product to be updated
#return: the product updated
#raise: error if the update fails
def update_product(product):
    try:
        connection = connect()
        db = connection['products']
        db.products.update_one({"_id": product["_id"]}, {"$set": product}, upsert=False)
        return product
    except:
        print("Could not update product")

#this function will delete a product in the database
#param: product: the product to be deleted
#return: the product deleted
#raise: error if the deletion fails
def delete_product(product):
    try:
        connection = connect()
        db = connection['products']
        db.products.delete_one(product)
        return product
    except:
        print("Could not delete product")

#this function will insert a new client in the database
#param: client: the client to be inserted
#return: the client inserted
#raise: error if the insertion fails
def insert_client(client):
    try:
        connection = connect()
        db = connection['clients']
        db.clients.insert_one(client)
        return client
    except:
        print("Could not insert client")

#this function will find a client in the database
#param: client: the client to be found
#return: the client found
#raise: error if the search fails
def find_client(client):
    try:
        connection = connect()
        db = connection['clients']
        return db.clients.find_one(client)
    except:
        print("Could not find client")

#this function will update a client in the database
#param: client: the client to be updated
#return: the client updated
#raise: error if the update fails
def update_client(client):
    try:
        connection = connect()
        db = connection['clients']
        db.clients.update_one({"_id": client["_id"]}, {"$set": client}, upsert=False)
        return client
    except:
        print("Could not update client")

#this function will delete a client in the database
#param: client: the client to be deleted
#return: the client deleted
#raise: error if the deletion fails
def delete_client(client):
    try:
        connection = connect()
        db = connection['clients']
        db.clients.delete_one(client)
        return client
    except:
        print("Could not delete client")
