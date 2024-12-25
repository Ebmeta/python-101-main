# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib

path = pathlib.Path('C:/Users/Наталия/Downloads/python-101-main/python-101-main')
print(path)
for f in path.glob("**/*"):
    if f.suffix == ".py":
        print(f.name)
