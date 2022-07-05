import datetime
from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class ItemSchema(BaseModel):
    id: Optional[int] = None
    day: Optional[int] = None
    date: Optional[datetime.date] = None
    troops: Optional[int] = None
    tanks: Optional[int] = None
    apv: Optional[int] = None
    ars: Optional[int] = None
    mlrs: Optional[int] = None
    aaws: Optional[int] = None
    airc: Optional[int] = None
    helic: Optional[int] = None
    uav: Optional[int] = None
    missiles: Optional[int] = None
    vehicle: Optional[int] = None
    fueltanks: Optional[int] = None
    warships_boats: Optional[int] = None
    specialequipment: Optional[int] = None
    srbm: Optional[int] = None
    
    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestItem(BaseModel):
    parameter: ItemSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
