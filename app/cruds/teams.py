from app.database import database
from app.schemas.teams import PostNewTeamRequest

class TeamsCRUD():
    """Teams CRUD"""
    async def get_team_info_by_team_id(self, team_id: int):
        """Get team info from database by team_id"""
        query = """
            SELECT *
            FROM "Team"
            WHERE "ID" = :team_id
            """

        # setup query variables
        values = {"team_id": team_id}
        # query the database
        data = await database.fetch_one(query=query, values=values)
        return data

    async def create_new_team(self, team_data: PostNewTeamRequest):
        """Create a new team by the team data."""
        # SELECT SCOPE_IDENTITY(); returns the latest ID
        query = """
            INSERT INTO public."Team" ("TeamName","DepartureDate","ReturnDate","GuideID","LeaderID")
                VALUES (:team_name, :departure_date, :return_date, :guide_id, :leader_id)
                RETURNING "ID";
            """

        values = {
            "team_name": team_data.TeamName,
            "departure_date": team_data.DepartureDate,
            "return_date": team_data.ReturnDate,
            "guide_id": team_data.GuideID,
            "leader_id": team_data.LeaderID
        }
        
        new_team_id = await database.execute(query=query, values=values)
        return new_team_id