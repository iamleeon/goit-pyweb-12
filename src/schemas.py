from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, Field


class ContactBase(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: str = Field(max_length=320)
    phone: str = Field(max_length=15)
    birthday: date
    additional_info: Optional[str] = Field(None, max_length=350)


class ContactCreate(ContactBase):
    pass  # All fields are inherited from ContactBase


class ContactUpdate(BaseModel):
    first_name: Optional[str] = Field(max_length=50)
    last_name: Optional[str] = Field(max_length=50)
    email: Optional[str] = Field(max_length=320)
    phone: Optional[str] = Field(max_length=15)
    birthday: Optional[date]
    additional_info: Optional[str] = Field(None, max_length=350)


class ContactResponse(ContactBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
