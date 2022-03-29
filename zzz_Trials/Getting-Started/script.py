import typer

def main(name: str='Weby', legacy:bool = False):
    print("Hello: ", name, "Legacy Parameter: ", legacy)

if __name__ == '__main__':
    typer.run(main)

# "python .\script.py --name Vaibhav" (Run this Command to pass Parameters from CLI)