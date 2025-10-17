try:
    import os
    from pathlib import Path
except ImportError as e:
    print("Error modulo__>",e)

cwd = os.getcwd()
custom_path = os.path.join(cwd,"python/sqlite/02_sql")
print(cwd)
DIR_DB = os.path.join(custom_path,"db/folder_db")
DIR_EXCEL =os.path.join(custom_path,"public/excel")
def create_dir():
    for dir in [DIR_DB,DIR_EXCEL]:
        if not os.path.exists(dir):
            os.makedirs(dir)

NAME_DB = "DB"