import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    # Приветствие пользователя
    print(f"Hello {name}")

app.command()
def goodbye(name: str, format: bool = False):
    # прощание с пользователем
    if formal:
        print(f"Goodbye Ms./Mr. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")

if __name__ == "__main__":
    app()

