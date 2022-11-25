"""Teams related schema."""
from datetime import date

from pydantic import BaseModel, Field


class GetTeamsInfoResponse(BaseModel):
    ID: int = Field(..., title="隊伍編號", description="隊伍編號")
    TeamName: str = Field(..., title="隊伍名稱", description="出隊的隊伍名稱")
    DepartureDate: date = Field(..., title="出發日期", description="隊伍的出發日期")
    ReturnDate: date = Field(..., title="回程日期", description="隊伍的預計下山日期")
    GuideID: int = Field(..., title="嚮導編號", description="開隊嚮導編號")
    LeaderID: int = Field(..., title="領隊編號", description="帶隊領隊編號")


class PostNewTeamRequest(BaseModel):
    TeamName: str = Field(..., title="隊伍名稱", description="出隊的隊伍名稱")
    DepartureDate: date = Field(..., title="出發日期", description="隊伍的出發日期")
    ReturnDate: date = Field(..., title="回程日期", description="隊伍的預計下山日期")
    GuideID: int = Field(..., title="嚮導編號", description="開隊嚮導編號")
    LeaderID: int = Field(..., title="領隊編號", description="帶隊領隊編號")

class PostNewTeamResponse(BaseModel):
    NewTeamID: int = Field(..., title="隊伍編號", description="隊伍編號")
