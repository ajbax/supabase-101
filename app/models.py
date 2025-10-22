# car model

from pydantic import BaseModel, EmailStr, Field, field_validator
from .forms import as_form

@as_form
class CarBase(BaseModel):    
    id: str
    created_at: str
    make: str
    model: str
    city: str

    @field_validator("make", "model", "city")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("Field cannot be empty")
        return v

@as_form
class CarCreate(CarBase):
    pass