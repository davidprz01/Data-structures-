from pydantic import BaseModel

class Ticket(BaseModel):
    name: str # name of the person
    type: str # type of consultation
    identity: str # identity card
    case_description: str # description of the case
    age: int # age of the person
    priority_attention: bool = None  # Will be calculated automatically

