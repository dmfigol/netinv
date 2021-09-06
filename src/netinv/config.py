from typing import TypeVar, Union, Dict, Any, Type

from pydantic import BaseSettings, PyObject

from netinv.device import Device
from netinv.exceptions import NetInvValueError

T = TypeVar("T", bound="NetInvConfig")

ConfigArgType = Union[Dict[str, Any], "NetInvConfig", None]


class NetInvConfig(BaseSettings):
    device_factory: PyObject = Device

    class Config:
        env_prefix = "netinv_"

    @classmethod
    def create(cls: Type[T], value: ConfigArgType = None) -> T:
        if value is None:
            result = cls()
        elif isinstance(value, dict):
            result = cls(**value)
        elif isinstance(value, cls):
            result = value
        else:
            raise NetInvValueError(
                f"Can't convert argument of type "
                f"{value.__class__.__qualname__!r} to Config object"
            )
        return result
