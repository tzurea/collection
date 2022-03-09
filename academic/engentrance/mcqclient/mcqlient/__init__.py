import os
import appdirs
from pathlib import Path

def check_file(path):
    if path.exists():
        return path
    else:
        path.touch(exists_ok=False)


def check_path(path):
    if path.exists():
        return path
    else:
        path.mkdir(parents=True, exists_ok=False)


app_name = 'mcqlient'
app_author = 'mcqlient'


root_data_dir = appdirs.user_data_dir(appname=appname, appauthor=app_author)
root_data_dir = Path(root_data_dir)
root_data_dir = check_path(root_data_dir)

database_path = root_data_dir.join('database')
database_path = check_path(database_path)

database_file = database_path.join('data.db')
database_file = check_file(database_file)

