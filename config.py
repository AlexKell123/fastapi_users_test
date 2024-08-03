from repositories import RedisUserRepository, SqliteUserRepository

# Словарь, хранящий класс и настройки репозитория Redis
settings_redis = {'repository_type': RedisUserRepository,
                  'repository_settings': {'host': 'localhost', 'port': 6379, 'db': 0}
                  }

# Словарь, хранящий класс и настройки репозитория Sqlite
settings_sqlite = {'repository_type': SqliteUserRepository,
                   'repository_settings': {'database': 'users.db'}
                   }

# Переменная settings ссылается на словарь с настройками, в зависимости от выбора репозитория
settings = settings_redis
# settings = settings_sqlite
