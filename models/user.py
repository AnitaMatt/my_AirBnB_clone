""" User that inherits from BaseModel"""
from models.base_model import BaseModel

class User(BaseModel):
    """Users"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""