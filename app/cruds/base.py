from databases import Database


class BaseCRUD:
    def __init__(self, db: Database):
        self.db = db
