from app import app
import view

from posts.blueprint import posts

from app import db


app.register_blueprint(posts, url_prefix='/news')


if __name__ == '__main__':
    app.run()
