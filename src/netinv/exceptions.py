class NetInvError(Exception):
    pass


class NetInvValueError(NetInvError, ValueError):
    pass
