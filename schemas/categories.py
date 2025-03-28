from pydantic import BaseModel, Field, ConfigDict

class CategoryBase(BaseModel):
    id: int
    name: str = Field(..., min_length=5)
    model_config = ConfigDict(
        from_attributes=True
    )