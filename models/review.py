#!/usr/bin/python3
"""Defines the Review class."""
# Importing necessary modules
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.
    
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    # Initializing attributes
    place_id = ""
    user_id = ""
    text = ""

