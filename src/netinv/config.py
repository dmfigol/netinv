from typing import TypeVar

from pydantic import BaseSettings, PyObject

from netinv.device import Device

T = TypeVar("T", bound="Device")


class Config(BaseSettings):
    device_factory: PyObject = Device

    class Config:
        env_prefix = "netinv_"
