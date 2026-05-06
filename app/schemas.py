from pydantic import BaseModel
from typing import Optional
class CrewBase(BaseModel):
    name: str
    captain: str
    ship: str
    is_active: bool = True
class CrewCreate(CrewBase):
    pass
class CrewUpdate(BaseModel):
    name: Optional[str] = None
    captain: Optional[str] = None
    ship: Optional[str] = None
    is_active: Optional[bool] = None
class CrewResponse(CrewBase):
    id: int
    class Config:
        from_attributes = True
class CharacterBase(BaseModel):
    name: str
    role: str
    bounty: int
    crew_id: int
class CharacterCreate(CharacterBase):
    pass
class CharacterUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    bounty: Optional[int] = None
    crew_id: Optional[int] = None
class CharacterResponse(CharacterBase):
    id: int
    class Config:
        from_attributes = True