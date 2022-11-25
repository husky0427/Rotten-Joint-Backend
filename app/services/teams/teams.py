"""Teams related service (logic level)."""
from app.cruds.teams import TeamsCRUD
from app.schemas.teams import PostNewTeamRequest

class TeamsService:
    """Teams service"""
    async def get_team_info(self, team_id: int):
        """Get team info logic."""
        team_info = await TeamsCRUD().get_team_info_by_team_id(team_id=team_id)
        return team_info

    async def create_new_team(self, request: PostNewTeamRequest):
        """Create a new team."""
        new_team_id = await TeamsCRUD().create_new_team(request)
        return new_team_id