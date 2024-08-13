import importlib
import sys
import os

error_handlers_modules = {'uvicorn': '.uvicorn_error_handler',
                          'console_app.py': '.console_app_error_handler'}

importing_script_name = os.path.basename(sys.argv[0])
error_handler_module = importlib.import_module(error_handlers_modules[importing_script_name], "error_handlers")

error_handler = getattr(error_handler_module, 'error_handler')

