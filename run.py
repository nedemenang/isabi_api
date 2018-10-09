from app.utils import db
from config import get_env
from app import create_app
from flask_script import Manager
# from app.utils.auth import Auth
from flask_migrate import Migrate, MigrateCommand

app = create_app("development")
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

# Creates the db tables
@manager.command
def create_db():
	db.create_all()


# Drops the db tables
@manager.command
def drop_db():
	db.drop_all()


if __name__ == '__main__':
	manager.run()
