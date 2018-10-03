#inside resources create a python file for the entity
from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        #get from models
        store = StoreModel.find_by_name(name)
        #if got
        if store:
            return store.json()
        #else
        return {'message': 'Store not found'}, 404

    def post(self, name):
        #check if already exists by get request with the name
        if StoreModel.find_by_name(name):
            return {'message': 'A Store with name {} already there in database. Use another name.'.format(name)}, 400
        #if not there we proceed to put
        #we put the data and convert in an object of the type that would match the structure in database table and also to create a json output to return as success message
        #create object name store using class StoreModel in Models folder
        store = StoreModel(name)
        #try to save using save function created in StoreModel
        try:
            store.save_to_db()
        except:
            #return error if something goes wrong and save function is not completed
            return {'message': 'An error occured while creating the store.'}, 500
        #convert object to json using a function defined in StoreModel class in store.py in Models folder
        return store.json(), 201

    def put(self, name):
        pass

    def delete(Self, name):
        #find store with name in database
        store = StoreModel.find_by_name(name)
        #if found then delete
        if store:
            store.delete_from_db()
        else:
        #if not such record, then inform
            return {'message': 'No such record with name {}'.format(name)}, 201
        #else give success message
        return {'message': 'Store named {} deleted'.format(name)}, 201

#Get All Stores
class StoreList(Resource):
    def get(self):
        #get all and return in json format
        return {'stores': [store.json() for store in StoreModel.query.all()]}
