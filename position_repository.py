from user_repository_config import user_repository_config
from user_repository_redis import UserRepositoryRedis
from user_repository_sqlite import UserRepositorySqlite


def user_repository_init(config):
    repository_type = config['repository_type']
    repository_settings = config['repository_settings']
    return repository_type(*repository_settings.values())


user_repository = user_repository_init(user_repository_config)
