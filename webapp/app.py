from datetime import datetime
from flask import Flask, jsonify, request

from database import db_session, init_db
from models import User

app = Flask(__name__)
init_db()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/users")
def hello():
    return jsonify([x.json_rep() for x in User.query.all()])


@app.route("/create", methods=['POST'])
def add_user():
    req_data = request.get_json()
    if req_data is None:
        return jsonify("empty request body"), 400

    email = req_data.get('email')
    if email is None:
        return jsonify("email is required in request body"), 400

    if db_session.query(User.id).filter_by(email=email).scalar() is not None:
        return jsonify("user already created"), 400

    u = User(email)
    u.first_name = req_data.get('first_name')
    u.last_name = req_data.get('last_name')
    u.created_at = datetime.now()
    u.updated_at = datetime.now()

    db_session.add(u)
    db_session.commit()

    return jsonify(u.json_rep()), 201


@app.route("/update",  methods=['PATCH'])
def update_user():
    req_data = request.get_json()
    if req_data is None:
        return jsonify("req_data problem"), 400

    email = req_data['email']
    u = User.query.filter(User.email == email).first()
    if u is None:
        return jsonify("user not found"), 400

    if req_data.items() is None:
        return jsonify("empty request"), 400

    u.assign_properties(**req_data)
    u.updated_at = datetime.now()

    db_session.commit()

    return jsonify(u.json_rep())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
