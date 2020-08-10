from typing import Protocol

import werkzeug


class ContextProto(Protocol):
    hostname: str


class EventProto(Protocol):
    body: bytes
    headers: werkzeug.datastructures.EnvironHeaders
    method: str
    query: werkzeug.datastructures.ImmutableMultiDict
    path: str
