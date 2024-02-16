#!/usr/bin/python3
"""Defines the City class."""
# Importing necessary modules
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.
    
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    # Initializing attributes
    state_id = ""
    name = ""

