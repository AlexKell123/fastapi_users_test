import click
from controllers import user_controller, position_controller


@click.group()
def cli():
    pass


@cli.command()
@click.option('--full_name', prompt='Enter user name', help='User Name')
@click.option('--email', prompt='Enter user email', help='User Email')
def create_user(full_name: str, email: str):
    """Create user"""
    result = user_controller.create(full_name, email)
    click.echo(result)


@cli.command()
@click.option('--user_id', prompt='Enter user ID', help='User ID')
def read_user(user_id: int):
    """Read user information"""
    result = user_controller.read(user_id)
    click.echo(result)


@cli.command()
@click.option('--user_id', prompt='Enter user ID', help='User ID')
@click.option('--full_name', prompt='Enter new name', help='New Name')
@click.option('--email', prompt='Enter new email', help='New Email')
def update_user(user_id: int, full_name: str, email: str):
    """Update user information"""
    result = user_controller.update(user_id, full_name, email)
    click.echo(result)


@cli.command()
@click.option('--user_id', prompt='Enter user ID', help='User ID')
def delete_user(user_id: int):
    """Delete a user"""
    result = user_controller.delete(user_id)
    click.echo(result)


@cli.command()
@click.option('--title', prompt='Enter title', help='Title')
def create_position(title: str):
    """Create position"""
    result = position_controller.create(title)
    click.echo(result)


@cli.command()
@click.option('--position_id', prompt='Enter position ID', help='Position ID')
def read_position(position_id: int):
    """Read position information"""
    result = position_controller.read(position_id)
    click.echo(result)


@cli.command()
@click.option('--position_id', prompt='Enter position ID', help='Position ID')
@click.option('--title', prompt='Enter new title', help='New title')
def update_position(position_id: int, title: str):
    """Update position information"""
    result = position_controller.update(position_id, title)
    click.echo(result)


@cli.command()
@click.option('--position_id', prompt='Enter position ID', help='Position ID')
def delete_position(position_id: int):
    """Delete a position"""
    result = position_controller.delete(position_id)
    click.echo(result)


if __name__ == '__main__':
    cli()
