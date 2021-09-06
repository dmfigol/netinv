import os

from netinv.device import Device
from netinv.exceptions import NetInvValueError
from netinv.config import NetInvConfig
from typing import Dict, Any

import pytest
from pydantic.types import NoneStr


class MyDevice(Device):
    test_atr: NoneStr


class TestConfig:
    @pytest.mark.parametrize(
        "args, expected_attrs",
        (
            ({}, {"device_factory": Device}),
            ({"device_factory": "test_config.MyDevice"}, {"device_factory": MyDevice}),
            ({"device_factory": MyDevice}, {"device_factory": MyDevice}),
        ),
    )
    def test_init(self, args: Dict[str, Any], expected_attrs: Dict[str, Any]):
        cfg = NetInvConfig.parse_obj(args)
        for key, value in expected_attrs.items():
            assert getattr(cfg, key) == value

    @pytest.fixture
    def setup_teardown_env(self):
        os.environ["netinv_device_factory"] = "test_config.MyDevice"
        yield
        os.environ.pop("netinv_device_factory", None)

    def test_env(self, setup_teardown_env):
        cfg = NetInvConfig()
        assert cfg.device_factory == MyDevice

    @pytest.mark.parametrize(
        "arg",
        [None, {"device_factory": MyDevice}, NetInvConfig(device_factory=MyDevice)],
    )
    def test_parse_arg(self, arg):
        cfg = NetInvConfig.create(arg)
        assert isinstance(cfg, NetInvConfig)

    @pytest.mark.parametrize("arg", [[("device_factory", MyDevice)]])
    def test_parse_arg_fail(self, arg):
        assert pytest.raises(NetInvValueError, NetInvConfig.create, arg)
