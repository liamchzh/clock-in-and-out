from flask import jsonify, request, make_response
from flask_restful import Resource, Api

from .models import create_clock_event
from .models import delete_clock_event
from .models import get_all_clock_events
from .models import get_event
from .models import get_clock_event_by_user
from .models import validate_user

api = Api()

class Login(Resource):

    def post(self):
        body = request.json
        email = body["email"]
        password = body["password"]
        result = validate_user(email, password)
        if result:
            resp = make_response("200")
            resp.set_cookie('user_id', '1', secure=True)
            return resp
        else:
            return "Wrong Email or password", 401


class User(Resource):

    def get(self):
        user_id = request.cookies.get('user_id')
        if not user_id:
            return "User Not Found", 404
        user = {"user_id": user_id, "user_name": "user_name"}
        return jsonify(user)


class UserClockEvent(Resource):

    def get(self, user_id):
        events = get_clock_event_by_user(user_id)
        return jsonify(events)


class ClockEvents(Resource):

    def get(self):
        events = get_all_clock_events()
        return jsonify(events)

    def post(self):
        event_id = create_clock_event()
        event = get_event(event_id)
        return jsonify(event)


class Event(Resource):

    def put(self, event_id):
        # TBD
        return jsonify({})

    def delete(self, event_id):
        delete_clock_event(event_id)
        return "", 204


api.add_resource(Login, '/login')
api.add_resource(User, '/user')
api.add_resource(UserClockEvent, '/user/<string:user_id>/clock-events')
api.add_resource(ClockEvents, '/clock-events')
api.add_resource(Event, '/clock-events/<string:event_id>')
