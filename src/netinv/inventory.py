from types import TracebackType
from typing import (
    TypeVar,
    Dict,
    Sequence,
    Union,
    Optional,
    Type,
    Any,
    TYPE_CHECKING,
)
from typing_extensions import Literal

from netinv.config import NetInvConfig

if TYPE_CHECKING:
    from netinv.config import ConfigArgType
    from netinv.device import Device


T = TypeVar

DevicesArgs = Union[
    Dict[str, Dict[str, Any]],
    Sequence[Dict[str, Any]],
    Dict[str, "Device"],
    Sequence["Device"],
    None,
]


class BaseInventory:
    # name_to_device: Dict[str]
    # config: Config
    def __init__(
        self, devices: DevicesArgs = None, config: "ConfigArgType" = None
    ) -> None:
        self.config = NetInvConfig.create(config)

        # factory = self.config.device_factory


class Inventory(BaseInventory):
    def __init__(self, devices: DevicesArgs, config: NetInvConfig) -> None:
        super().__init__(devices=devices, config=config)

    def __enter__(self) -> "Inventory":
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> Literal[False]:
        return False


class AsyncInventory(BaseInventory):
    def __init__(self, devices: DevicesArgs, config: NetInvConfig) -> None:
        super().__init__(devices=devices, config=config)

    def __aenter__(self) -> "AsyncInventory":
        return self

    def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> Literal[False]:
        return False
