import click

@click.command()
@click.argument('rnumber')
@click.option("--writefile", is_flag=True, help="Output to file")
def query_api(rnumber, writefile):
    """Access the Panel-APP Api."""
    #return_value= function(rnumber)

    click.echo('Accessing the Panel-APP Api...')
    click.echo(f'Rnumber: {rnumber}')
    if writefile:
        with open('output.txt', 'w') as f:
            f.write(rnumber)



    pass
if __name__ == '__main__':
    query_api()

