from pydantic import BaseModel


class OrderCreate(BaseModel):
    customer: str
    amount: float