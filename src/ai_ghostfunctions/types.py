"""Datatypes for ai-ghostfunctions."""

from typing import Literal
from typing import TypedDict


CompletionType = Literal["completion", "chat completion"]
RoleType = Literal["system", "user", "assistant"]


class Message(TypedDict):
    """A single message sent to the OpenAI API for a ChatCompletion."""

    role: RoleType
    content: str
