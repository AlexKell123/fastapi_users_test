class Settings:
    # DB_TYPE = 'DB_REDIS'
    DB_TYPE = 'DB_SQLITE'

    MODULES = {'DB': {'DB_REDIS': 'src.repositories.db_redis.db',
                      'DB_SQLITE': 'src.repositories.db_sqlite.db',
                      },
               'ERROR_HANDLER_FASTAPI': 'src.error_handlers.error_handler_fastapi',
               'ERROR_HANDLER_CLI': 'src.error_handlers.error_handler_cli',
               'CONTROLLERS': ['src.controllers.user_controller',
                               'src.controllers.position_controller'
                               ],

               'REPOSITORIES': {'DB_REDIS': ['src.repositories.db_redis.user_repository',
                                             'src.repositories.db_redis.position_repository',
                                             ],
                                'DB_SQLITE': ['src.repositories.db_sqlite.user_repository',
                                              'src.repositories.db_sqlite.position_repository',
                                              ],
                                },

               'ROUTERS': ['src.fastapi_app.user_router',
                           'src.fastapi_app.position_router',
                           ],
               'NOTIFICATION': 'src.notifications.email_notification',
               }

    DB_CFG = {'DB_REDIS': {'host': 'localhost', 'port': 6379, 'db': 0},
              'DB_SQLITE': {'db_name': 'test1.db'},
              }
