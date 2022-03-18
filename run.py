from flask import Flask

from app.posts.views import main_blueprint
from app.api.views import api_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)


if __name__ == "__main__":
    app.run()
