from datetime import datetime

from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import Cheese, Producer, db
from werkzeug.exceptions import NotFound


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)


# @app.route("/")
# def index():
#     response = make_response({"message": "Hello Fromagers!"}, 200)
#     return response


class Index(Resource):
    def get(self):
        return {"message": "Hello Fromagers!"}, 200


class Producers(Resource):
    def get(self):
        producers = [p.to_dict(rules=("-cheeses",)) for p in Producer.query]
        return jsonify(producers), 200


class ProducersById(Resource):
    def get(self, id):
        producer = Producer.query.get_or_404(id)
        return jsonify(producer.to_dict()), 200

    def delete(self, id):
        producer = Producer.query.get_or_404(id)
        db.session.delete(producer)
        db.session.commit()
        return "", 204


class Cheeses(Resource):
    def post(self):
        data = request.get_json()
        try:
            cheese = Cheese(**data)
        except ValueError as e:
            return jsonify({"error": e.args}), 422

        db.session.add(cheese)
        db.session.commit()
        return (
            jsonify(
                cheese.to_dict(
                    rules=(
                        "-producer.founding_year",
                        "-producer.region",
                        "-producer.operation_size",
                        "-producer.image",
                        "-producer.id",
                    )
                )
            ),
            201,
        )


class CheesesById(Resource):
    def patch(self, id):
        cheese = Cheese.query.get_or_404(id)
        data = request.get_json()
        for k, v in data.items():
            if k == "production_date":
                v = datetime.strptime(v, "%Y-%m-%d")
            setattr(cheese, k, v)
        db.session.commit()
        return jsonify(cheese.to_dict(rules=("-producer",))), 200

    def delete(self, id):
        cheese = Cheese.query.get_or_404(id)
        db.session.delete(cheese)
        db.session.commit()
        return "", 204


api.add_resource(Producers, "/producers")
api.add_resource(ProducersById, "/producers/<int:id>")
api.add_resource(Cheeses, "/cheeses")
api.add_resource(CheesesById, "/cheeses/<int:id>")


@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": "Resource not found"}), 404


if __name__ == "__main__":
    app.run(port=5555, debug=True)
