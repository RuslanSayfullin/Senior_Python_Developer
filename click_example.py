import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    cli()

# $ python app.py hello John
# Hello John!

# $ python3 app.py hello Kate --count=3
# Hello Kate!
# Hello Kate!
# Hello Kate!
