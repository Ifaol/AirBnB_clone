#!/usr/bin/python3
"""Defines the State class."""
# Importing necessary modules
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.
    
    Attributes:
        name (str): The name of the state.
    """

    # Initializing attributes
    name = ""

