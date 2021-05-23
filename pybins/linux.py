from tinydb import TinyDB, Query
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.syntax import Syntax
from pybins.data import get_db_path


def get_data(fragment):
    db = TinyDB(get_db_path())
    db_query = Query()
    data = db.search(db_query.fragment(fragment))
    return data

def get_platform_binaries():
    fragment = { 
            'platform' : 'linux'
            }
    data = get_data(fragment)
    binaries = []
    for snip in data:
        if snip['cmd'] not in binaries:
            binaries.append(snip['cmd'])
    return binaries

def get_platform_functions():
    fragment = { 
            'platform' : 'linux'
            }
    data = get_data(fragment)
    functions = []
    for snip in data:
        if snip['function'] not in functions:
            functions.append(snip['function'])

    return functions

def get_binary_functions(binary):
    fragment = {
            'platform': 'linux',
            'cmd': binary
            }
    data = get_data(fragment)
    functions = []
    for snip in data:
        if snip['function'] not in functions:
            functions.append(snip['function'])

    return functions


def get_function_binaries(function):
    fragment = { 
            'platform' : 'linux',
            'function' : function
            }
    data = get_data(fragment)
    binaries = []
    for snip in data:
        if snip['cmd'] not in binaries:
            binaries.append(snip['cmd'])
    return binaries

def get_binary_cmd(binary, function):
    fragment = {
            'platform' : 'linux',
            'cmd'      : binary,
            'function' : function
            }
    data = get_data(fragment)
    return data[0]['data']

def print_binary_functions(binary):
    console = Console()
    print = console.print
    functions = get_binary_functions(binary)
    columns = Columns(functions, equal=True, expand=True)
    print(f"The binary [bold red]{binary}[/bold red] has the following categories:\n",
          columns,
          "\n")

def print_function_binaries(function):
    console = Console()
    print = console.print
    functions = get_function_binaries(function)
    columns = Columns(functions, equal=True, expand=True)
    print(f"The Function [bold red]{function}[/bold red] has the following binaries:\n",
          columns,
          "\n")

def print_binary_cmd(binary, function):
    console = Console()
    print = console.print
    data = get_binary_cmd(binary, function)
    for snip in data:
        grid = Table.grid()
        grid.add_column()
        grid.add_column()
        if 'description' in snip:
            grid.add_row("Description:  ", snip['description'])
        if 'code' in snip:
            grid.add_row("Command:      ", Syntax(snip['code'], "shell") )
        print(grid, "\n")


def print_platform_binaries():
    console = Console()
    print = console.print
    binaries = get_platform_binaries()
    columns = Columns(binaries, equal=True, expand=True)
    print(f"[bold red]Linux GTFO[/bold red] has the following binaries:\n",
          columns,
          "\n")

def print_platform_functions():
    console = Console()
    print = console.print
    functions = get_platform_functions()
    columns = Columns(functions, equal=True, expand=True)
    print(f"[bold red]Linux GTFO[/bold red] has the following categories:\n",
          columns,
          "\n")

def print_platform_all():
    print_platform_binaries()
    print_platform_functions()


