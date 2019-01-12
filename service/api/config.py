from os import environ
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:

    # TODO: inherit this from base (service) config
    # b/c its common for db and api
    dsn: str = environ.get(
        'SERVICE_DSN', 
        'postgresql://postgres:@localhost:5432/service'        
    )
