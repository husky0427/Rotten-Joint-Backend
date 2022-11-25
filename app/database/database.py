from databases import Database

from app.configurations import DatabaseConf

DB_URL = '%s://%s:%s@%s/%s?charset=utf8' % (
    DatabaseConf.DBMS,
    DatabaseConf.USERNAME,
    DatabaseConf.PASSWORD,
    DatabaseConf.HOST,
    DatabaseConf.DATABASE,
)

database = Database(DB_URL, min_size=5, max_size=20)
