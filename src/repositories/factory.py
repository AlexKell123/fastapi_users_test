from src.repositories.db_redis import DBRedis, UserRepositoryRedis, PositionRepositoryRedis
from src.repositories.db_sqlite import DBSqlite, UserRepositorySqlite, PositionRepositorySqlite


class DBFactory:
    @staticmethod
    def get(config):
        db_types = {'DB_REDIS': DBRedis,
                    'DB_SQLITE': DBSqlite
                    }
        return db_types[config.db_type](*config.db_cfg)


class RepositoryFactory:
    @staticmethod
    def get(db, error_handler, model_name):
        db_types = {'DB_REDIS': {'user': UserRepositoryRedis,
                                 'position': PositionRepositoryRedis},
                    'DB_SQLITE': {'user': UserRepositorySqlite,
                                  'position': PositionRepositorySqlite},
                    }
        return db_types[db.type][model_name](db, error_handler)
