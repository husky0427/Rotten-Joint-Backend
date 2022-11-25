from smtplib import SMTPSenderRefused
from typing import Optional, Union

from pydantic import BaseModel, Field


class Expenditure(BaseModel):
    ItemID: int = Field(..., title="帳目編號", description="項目編號")
    Expenditure: str = Field(..., title="支出", description="支出項目")
    Spender: str = Field(..., title="支出者", description="付錢的人")
    Cost: int = Field(..., title="支出花費", description="花費多少新台幣")


class AccountsRequest(BaseModel):
    team_id: int = Field(..., description="Team Id")
