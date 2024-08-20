from src.error_handlers import ErrorHandlerCli, ErrorHandlerFastapi


class ErrorHandlerFactory:
    @staticmethod
    def get(gateway_type):
        gateway_types = {'Fastapi': ErrorHandlerFastapi,
                         'Cli': ErrorHandlerCli
                         }
        return gateway_types[gateway_type]()
