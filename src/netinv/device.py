from typing import Set, Dict
from pydantic import BaseModel, Field
from pydantic.types import OptionalInt, NoneStr


class ConnectionOptions(BaseModel):
    name: str
    type: NoneStr
    host: NoneStr
    port: OptionalInt
    platform: NoneStr


class Device(BaseModel):
    name: str
    host: NoneStr
    username: NoneStr
    password: NoneStr
    platform: NoneStr
    tags: Set[str] = set()
    connection_options: Dict[str, ConnectionOptions] = Field(
        alias="connections", default_factory=dict
    )
