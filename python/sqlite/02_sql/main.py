from core import config
from db import manager
config.create_dir()
manager.DBManager(config.NAME_DB)