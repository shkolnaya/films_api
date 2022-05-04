from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from src import db


from src.database.models import Actor
from src.schemas.actors import ActorSchema


class ActorListApi(Resource):
    actor_schema = ActorSchema()

    def get(self, uuid=None):
        if not uuid:
            actors = db.session.query(Actor).all()
            return self.actor_schema.dump(actors, many=True), 200
        actor = db.session.query(Actor).filter_by(uuid=uuid).first()
        if not actor:
            return '', 404
        return self.actor_schema.dump(actor), 200

    def post(self):
        try:
            actor = self.actor_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 201

    def put(self, uuid):
        actor = db.session.query(Actor).filter_by(uuid=uuid).first()
        if not actor:
            return {'message': 'Wrong data'}, 400
        try:
            actor = self.actor_schema.load(request.json, instance=actor, session=db.session, partial=False)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return self.actor_schema.dump(actor), 200

    def patch(self, uuid):
        actor = db.session.query(Actor).filter_by(uuid=uuid).first()
        if not actor:
            return '', 404
        try:
            actor = self.actor_schema.load(request.json, instance=actor, session=db.session, partial=True)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(actor)
        db.session.commit()
        return {'message': "Updated successfully"}, 201

    def delete(self, uuid):
        actor = db.session.query(Actor).filter_by(uuid=uuid).first()
        if not actor:
            return '', 404
        db.session.delete(actor)
        db.session.commit()
        return '', 204
