from user_repository_redis import UserRepositoryRedis
from user_repository_sqlite import UserRepositorySqlite

user_repository_config_redis = {'repository_type': UserRepositoryRedis,
                                'repository_settings': {'host': 'localhost', 'port': 6379, 'db': 0}
                                }

user_repository_config_sqlite = {'repository_type': UserRepositorySqlite,
                                 'repository_settings': {'database': 'users.db'}
                                 }

user_repository_config = user_repository_config_redis
# user_repository_config = user_repository_config_sqlite
