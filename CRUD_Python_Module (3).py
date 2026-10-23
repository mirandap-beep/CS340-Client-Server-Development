# Python CRUD Module for the Austin Animal Center database

from pymongo import MongoClient


class AnimalShelter(object):
    """CRUD operations for the Animal collection in MongoDB."""

    def __init__(self, username, password):
        # Connection variables for the AAC database
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize the MongoDB connection
        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT)
        )
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create method to implement the C in CRUD
    def create(self, data):
        """Insert a new document into the animals collection."""
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("An error occurred while inserting the document:", e)
                return False
        else:
            return False

    # Read method to implement the R in CRUD
    def read(self, query):
        """Query documents from the animals collection."""
        if query is not None:
            try:
                results = self.collection.find(query)
                return list(results)
            except Exception as e:
                print("An error occurred while reading the documents:", e)
                return []
        else:
            return []
        
    #Update method to implement U in CRUD
    def update(self, query, new_data):
        """Update documents in the animals collection."""
        if query is not None and new_data is not None:
            try: 
                result = self.collection.update_many(
                    query,
                    {"$set": new_data}
                )
                return result.modified_count
            except Exception as e:
                print("An error occured while updating the documents:", e)
                return 0
            else:
                return 0
                
    #Delete method to implement D in CRUD
    def delete(self, query):
        """Delete documents from the animals collection."""
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("An error occured while deleting the documents:", e)
                return 0
            else:
                return 0