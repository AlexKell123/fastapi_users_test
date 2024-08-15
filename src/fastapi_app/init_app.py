from fastapi import FastAPI, APIRouter
import importlib
from src.config import Settings


def init_app() -> FastAPI:
    def get_object(module_name, class_name, args=()):
        module = importlib.import_module(module_name)
        cls = getattr(module, class_name)
        return cls(*args)

    def get_repositories(db, error_handler):
        result = []
        for item in settings.MODULES['REPOSITORIES'][settings.DB_TYPE]:
            repository = get_object(item,
                                    'Repository',
                                    (db, error_handler))
            result.append(repository)
        return result

    def get_controllers(repositories, email_notification, error_handler):
        result = []
        for i, item in enumerate(settings.MODULES['CONTROLLERS']):
            controller = get_object(item,
                                    'Controller',
                                    (repositories[i], email_notification, error_handler))
            result.append(controller)
        return result

    def get_routers(controllers):
        router = APIRouter()
        for i, item in enumerate(settings.MODULES['ROUTERS']):
            new_router = get_object(item,
                                    'get_router',
                                    [controllers[i]])
            router.include_router(new_router)
        return router

    settings = Settings()
    db = get_object(settings.MODULES['DB'][settings.DB_TYPE],
                    'DB',
                    settings.DB_CFG[settings.DB_TYPE].values())
    error_handler = get_object(settings.MODULES['ERROR_HANDLER_FASTAPI'],
                               'ErrorHandler')
    repositories = get_repositories(db, error_handler)
    email_notification = get_object(settings.MODULES['NOTIFICATION'],
                                    'EmailNotification')
    controllers = get_controllers(repositories, email_notification, error_handler)
    routers = get_routers(controllers)
    application = FastAPI()
    application.include_router(routers)
    return application
