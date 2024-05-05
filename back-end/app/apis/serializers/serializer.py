# serializer.py
import json

class UserSerializer:
    @staticmethod
    def serialize(user):
        return json.dumps({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })

    @staticmethod
    def deserialize(json_data):
        data = json.loads(json_data)
        return {
            'id': data.get('id'),
            'username': data.get('username'),
            'email': data.get('email')
        }
