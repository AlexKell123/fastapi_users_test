from src.logger import log
from src.init_config import JsonConfigFactory
from src.repositories.factory import DBFactory, RepositoryFactory
from src.error_handlers import ErrorHandlerFactory
from src.notifications.email_notification import EmailNotification
from src.controllers import UserController, PositionController


def init_app(cfg_file_path, gateway_type):
    log(f'read config file "{cfg_file_path}"')
    config = JsonConfigFactory.get(cfg_file_path)
    log(f'config: (db_type = "{config.db_type}", db_cfg = "{config.db_cfg}")')
    log('create database connection')
    db = DBFactory.get(config)
    log(f'database connection: {db.type}')
    log(f'create ErrorHandler: {gateway_type}')
    error_handler = ErrorHandlerFactory.get(gateway_type)
    log(f'create Notification: {gateway_type}')
    email_notification = EmailNotification()
    log(f'create user_repository')
    user_repository = RepositoryFactory.get(db, error_handler, 'user')
    log(f'create position_repository')
    position_repository = RepositoryFactory.get(db, error_handler, 'position')
    log(f'create user_controller')
    user_controller = UserController(user_repository, email_notification, error_handler)
    log(f'create position_controller')
    position_controller = PositionController(position_repository)
    return [user_controller, position_controller]
