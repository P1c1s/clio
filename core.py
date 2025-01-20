import sys
import os
import json
from pathlib import Path
from colors import *

class Clio:

    def __init__(self):
        self.script_directory = Path(__file__).parent

    def display_help(self):
        print(f"{WHITEBOLD}Usage: clio [COMMAND]{NOCOLOR}")
        print(f"{WHITEBOLD}about        -  Show you some information about Clio{NOCOLOR}")
        print(f"{WHITEBOLD}cli          -  Launch Clio in command line mode{NOCOLOR}")
        print(f"{WHITEBOLD}help         -  Display information about Clio commands{NOCOLOR}")
        print(f"{WHITEBOLD}info         -  Show information about modules{NOCOLOR}")
        print(f"{WHITEBOLD}modules      -  Show list of modules{NOCOLOR}")
        print(f"{WHITEBOLD}unknown      -  ...{NOCOLOR}")
        print(f"{WHITEBOLD}version      -  Show the version of Clio{NOCOLOR}")

    def display_about(self):
        print(f"{WHITEBOLD}Clio is a helper for Linux users that makes it easy to remember Linux commands.")
        print(f"It is written in Python and built with a modular architecture, allowing each module to be added or removed at any time.{RED}")
        print("\n        | <- components")
        print("        |")
        print("        |            | <- module[1]")
        print("core <- | <- modules | <- module[2]")
        print("        |            | <- module[n]")
        print("        |")
        print("        | <- ...")

    def list_modules(self):
        print(f"{WHITEBOLD}MODULES{NOCOLOR}")
        # Get the list of files and directories in the specified directory
        path = self.script_directory / 'modules'
        content = list(path.iterdir())
        sorted_content = sorted(path.iterdir(), key=lambda x: x.name.lower())
        # Display only the names of files without extensions
        for item in sorted_content:
            if item.is_file():  # Check if the item is a file
                self.check_module(item)

    def check_module(self, item):
        try:
            with open(item, 'r') as file:
                # Try to parse the JSON file
                json.load(file)
            print(f"{GREENBOLD}[+] {item.stem}{NOCOLOR}")  # Print only the file name without the extension
        except json.JSONDecodeError as e:
            # If there's an error in parsing, the file contains invalid JSON
            print(f"{REDBOLD}[-] {item.stem}{NOCOLOR}   {e}")  # Print only the file name without the extension
        except FileNotFoundError:
            print(f"The file {item} does not exist.")

    def display_module_info(self, module_name):
        path = self.script_directory / 'modules' /f'{module_name}.json'
        if path.exists():
            with open(path, 'r') as file:
                data = json.load(file)
                for category in data['categories']:
                    print()
                    print(f"{REDBOLD}{category['category']}{NOCOLOR}")
                    for command in category['commands']:
                        print(f"{WHITEBOLD}{command['command'].ljust(30)} - {WHITE} {command['description']}{NOCOLOR}")
        else:
            print("Unknown command")

    def run(self):
        if len(sys.argv) > 1:
            first_argument = sys.argv[1]  # First argument after the script name
            if first_argument == "help":
                self.display_help()
            elif first_argument == "about":
                self.display_about()
            elif first_argument == "modules":
                self.list_modules()
            else:
                self.display_module_info(first_argument)
        else:
            print(f"Hi, I am {WHITEBOLD}Clio{WHITE}. How can I help you?")
            print(f"Type {GREENBOLD}clio help{NOCOLOR} to see the list of commands.")

if __name__ == "__main__":
    clio = Clio()
    clio.run()
