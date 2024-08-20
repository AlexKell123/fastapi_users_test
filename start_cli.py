from src.init_app import init_app
from src.gateways import get_cli
from src.logger import log


log('starting cli init')
controllers = init_app('config.json', 'Cli')

log('add commands')
cli = get_cli(*controllers)


log('start cli')
if __name__ == '__main__':
    cli()
