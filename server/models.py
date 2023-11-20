from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata, engine_options={"echo": True})


class TimestampMixin:
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )


class Producer(db.Model, SerializerMixin, TimestampMixin):
    __tablename__ = "producers"

    serialize_rules = ("-cheeses.producer", "-created_at", "-updated_at")

    id = db.Column(db.Integer, primary_key=True)
    founding_year = db.Column(db.Integer)
    name = db.Column(db.String)
    region = db.Column(db.String)
    operation_size = db.Column(db.String)
    image = db.Column(db.String)

    cheeses = db.relationship("Cheese", backref="producer", lazy=True, cascade="delete")

    def __repr__(self):
        return f"<Producer {self.id}>"

    @validates("name")
    def validate_name(self, key, name):
        if not name:
            raise AssertionError("No name provided")
        if Producer.query.filter(Producer.name == name).first():
            raise AssertionError("Name is already in use")
        if len(name) > 50:
            raise AssertionError("Name must be less than 50 characters")
        return name

    @validates("founding_year")
    def validate_founding_year(self, key, founding_year):
        if not founding_year:
            raise AssertionError("No founding year provided")
        if founding_year < 1900 or founding_year > datetime.now().year:
            raise AssertionError("Founding year must be between 1900 and present")
        return founding_year

    @validates("operation_size")
    def validate_operation_size(self, key, operation_size):
        if not operation_size:
            raise AssertionError("No operation size provided")
        if operation_size not in ["small", "medium", "large", "family", "corporate"]:
            raise AssertionError(
                "Operation size must be one of 'small', 'medium', 'large', 'family', 'corporate'"
            )
        return operation_size


class Cheese(db.Model, SerializerMixin, TimestampMixin):
    __tablename__ = "cheeses"

    serialize_rules = ("-producer.cheeses", "-created_at", "-updated_at")

    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String)
    is_raw_milk = db.Column(db.Boolean)
    production_date = db.Column(db.DateTime)
    image = db.Column(db.String)
    price = db.Column(db.Float)

    producer_id = db.Column(db.Integer, db.ForeignKey("producers.id"), nullable=False)

    def __repr__(self):
        return f"<Cheese {self.id}>"

    @validates("price")
    def validate_price(self, key, price):
        if not price:
            raise AssertionError("No price provided")
        if not 1.00 <= price <= 45.00:
            raise AssertionError("Price must be between 1.00 and 45.00")
        return price

    @validates("production_date")
    def validate_production_date(self, key, date):
        production_date = datetime.strptime(f"{date}", "%Y-%m-%d")
        if production_date >= datetime.now():
            raise ValueError("Production date must be in the past")
        return production_date
