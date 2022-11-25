from app.database import database


class AccountCRUD:
    async def get_account_book_by(self, team_id):
        query = """
            SELECT "ItemID", "Expenditure", "Spender", "Cost"
            FROM "AccountBook"
            WHERE "TeamID" = :team_id
            ORDER BY "ItemID";
            """
        values = {"team_id": team_id}
        data = await database.fetch_all(query=query, values=values)
        # print([{**i} for i in data])
        return [{**i} for i in data]
