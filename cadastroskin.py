from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['items_db']
collection = db['items_collection']

class ItemCRUD:
    def create_item(self, price, rarity, pattern_index, disponibility):
        item = {
            'price': price,
            'rarity': rarity,
            'pattern_index': pattern_index,
            'disponibility': disponibility
        }
        result = collection.insert_one(item)
        return result.inserted_id

    def read_item(self, item_id):
        item = collection.find_one({'_id': item_id})
        return item

    def update_item(self, item_id, price, rarity, pattern_index, disponibility):
        result = collection.update_one(
            {'_id': item_id},
            {'$set': {
                'price': price,
                'rarity': rarity,
                'pattern_index': pattern_index,
                'disponibility': disponibility
            }}
        )
        return result.modified_count

    def delete_item(self, item_id):
        result = collection.delete_one({'_id': item_id})
        return result.deleted_count

    def sort_items(self):
        items = collection.find().sort([('rarity', 1), ('price', 1)])
        return list(items)
