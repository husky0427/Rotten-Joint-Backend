from fastapi import APIRouter

from app.schemas import APIResult, Response, GetTeamsInfoResponse, \
    PostNewTeamRequest, PostNewTeamResponse
from app.services.teams import TeamsService

router = APIRouter(
    prefix="/teams",
    tags=["teams"]
)

@router.get("/")
async def get_teams_page():
    return {"message": "You are in the teams home page!"}

@router.get("/{team_id}", response_model=Response[GetTeamsInfoResponse])
async def get_team_info(team_id: int):
    """GET a team's info by specifying the id of the team."""
    try:
        team_info = await TeamsService().get_team_info(team_id=team_id)
        response = Response(Result=APIResult.SUCCESS, DataObject=team_info)
    except Exception as e:
        response = Response(Result=APIResult.FAIL, message=f"{type(e).__name__}: {str(e)}")
    return response

@router.post("/new", response_model=Response[PostNewTeamResponse])
async def save_new_team_info(request: PostNewTeamRequest):
    """POST to /new to save a new team info"""
    try:
        new_team_id = await TeamsService().create_new_team(request)
        response_data = {
            "NewTeamID": new_team_id
        }
        response = Response(Result=APIResult.SUCCESS, DataObject=response_data)
    except Exception as e:
        response = Response(Result=APIResult.FAIL, message=f"{type(e).__name__}: {str(e)}")
    return response
