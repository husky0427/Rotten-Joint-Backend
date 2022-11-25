from typing import Generic, List, Optional, TypeVar
from unittest import result
from fastapi import APIRouter
from enum import IntEnum

from pydantic import Field
from pydantic.generics import GenericModel

T = TypeVar("T")


class APIResult(IntEnum):
    SUCCESS = 1
    FAIL = 2


class Response(GenericModel, Generic[T]):
    Result: APIResult = Field(description="Result Code")
    Message: str = Field(None, description="Result Message")
    DataObject: Optional[T] = Field(None, description="Result Object")
