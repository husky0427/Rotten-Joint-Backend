from app.cruds.account import AccountCRUD
from app.schemas import account


class AccountService:
    async def get_account_book(self, team_id: int):
        account_book_items = await AccountCRUD().get_account_book_by(team_id=team_id)
        return account_book_items
