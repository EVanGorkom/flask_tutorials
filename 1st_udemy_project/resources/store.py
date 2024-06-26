import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema


blue = Blueprint("stores", __name__, description="Operations on stores")

@blue.route("/store")
class StoreList(MethodView):
    @blue.reponse(200, StoreSchema(many=True))
    def get(self):
        return stores.values()
    
    @blue.arguments(StoreSchema)
    @blue.response(201, StoreSchema)
    def post(self, store_data):
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message=f"Store already exists.")
        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        return store, 201

@blue.route("/store/<string:store_id>")
class Store(MethodView):
    @blue.reponse(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "store deleted."}
        except KeyError:
            abort(404, message="store not found.")