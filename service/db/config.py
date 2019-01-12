from os import environ
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    """
    Immutable Config dataclass.
    """
    dsn:str = environ.get(
        'SERVICE_DSN', 
        'postgresql://postgres:@localhost:5432/service'
    )