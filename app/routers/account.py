from typing import List

from fastapi import APIRouter, Depends, Query

from app.schemas import APIResult, Response, Expenditure, AccountsRequest
from app.services.account import AccountService

router = APIRouter(
    prefix="/account",
    tags=["account"],
)


@router.post("/accounts", response_model=Response[List[Expenditure]])
async def get_all_expenditures(request: AccountsRequest):
    try:
        data = await AccountService().get_account_book(team_id=request.team_id)
        response = Response[List[Expenditure]](Result=APIResult.SUCCESS, DataObject=data)
    except Exception as e:
        response = Response(result=APIResult.FAIL, message=f"{type(e).__name__}: {str(e)}")
    return response
