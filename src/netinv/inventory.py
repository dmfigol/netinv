from types import TracebackType
from typing import TypeVar, Dict, Sequence, Union, Optional, Type, Any, TYPE_CHECKING
from pydantic import BaseModel, validate_arguments, parse_obj_as

from netinv.config import Config
from netinv.connections import Connections

if TYPE_CHECKING:
    from netinv.device import Device


T = TypeVar

DevicesArgs = Union[
    Dict[str, Dict[str, Any]],
    Sequence[Dict[str, Any]],
    Dict[str, "Device"],
    Sequence["Device"],
]


class BaseInventory:
    # name_to_device: Dict[str]
    # config: Config
    def __init__(
        self, devices: DevicesArgs, config: Union[Dict[str, Any], Config, None] = None
    ) -> None:
        if config is None:
            self.config = Config()
        elif isinstance(config, dict):
            self.config = Config(**config)
        else:
            self.config = config

        factory = self.config.device_factory


class Inventory(BaseInventory):
    def __init__(self, devices: DevicesArgs, config: Config) -> None:
        super().__init__(devices, config)

    def __enter__(self) -> "Inventory":
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> bool:
        return False


class AsyncInventory(BaseInventory):
    def __init__(self, devices: DevicesArgs, config: Config) -> None:
        super().__init__(devices, config)

    def __aenter__(self) -> "AsyncInventory":
        return self

    def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> bool:
        return False
