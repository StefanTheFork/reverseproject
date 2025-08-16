import platform
import psutil
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# funnifetch v1, make it yours...

def fetch():
    console = Console()
    # tribute to OG reverse. using all the official colours of it. red green blue and yelwo
    logo = """
    [bold red] _ __ _____   _____ _ __ ___  ___   [/bold red]
    [bold green]| '__/ _ \\ \\ / / _ \\ '__/ __|/ _ \\  [/bold green]
    [bold blue]| | |  __/\\ V /  __/ |  \\__ \\  __/ [/bold blue]
    [bold yellow]|_|  \\___| \\_/ \\___|_|  |___/\\___(_) [/bold yellow]
    """
    console.print(Panel.fit(logo, title="[bold magenta]funnifetch[/bold magenta]"))
    table = Table(show_header=False, show_lines=True)
    table.add_column("System Information", style="bold magenta")
    table.add_column("Value", style="bold yellow")
    table.add_row("host OS", platform.system())
    table.add_row("python version", platform.python_version())
    table.add_row("CPU cores", str(psutil.cpu_count(logical=False)))
    table.add_row("CPU threads", str(psutil.cpu_count(logical=True)))
    table.add_row("RAM", f"{psutil.virtual_memory().total / 2**30:.2f} GB")
    console.print(table)

