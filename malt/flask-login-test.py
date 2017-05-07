from flask import Flask
from flask import Response
from flask.ext.login import LoginManager
from flask.ext.login import UserMixin
from flask.ext.login import login_required
from db_connector import db_connection

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    # user_database = {"user1": ("user1", "1234")}
    #
    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password
    #
    # @classmethod
    # def get(cls, username):
    #     return cls.user_database.get(username)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_authenticated(self):
        return True


# @login_manager.request_loader
# def load_user(request):
    # token = request.headers.get('Authorization')
    # if token is None:
    #     token = request.args.get('token')
    #
    # if token is not None:
    #     username, password = token.split(':') #naive
    #     user_entry = User.get(username)
    #     if (user_entry is not None):
    #         user = User(user_entry[0],user_entry[1])
    #         if (user.password == password):
    #             return user
    # return None


@login_manager.user_loader
def load_user(username):
    u = db_connection()
    print(u[0]['userName'], u[0]['userPassword'])
    return User(u[0]['userName'], u[0]['userPassword'])


@app.route('/')
def index():
    return Response(response='Hello World', status=200)


@app.route('/protected')
@login_required
def protected():
    return Response(response='Protected World', status=200)


if __name__ == '__main__':
    app.config["SECRET_KEY"] = "ITSASECRET"
    app.run(port=5000,debug=True)
