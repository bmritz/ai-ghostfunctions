"""Keywords for ai-ghostfunctions."""
from typing import get_args

from .types import CompletionType
from .types import RoleType


COMPLETION, CHAT_COMPLETION = get_args(CompletionType)
SYSTEM, USER, ASSISTANT = get_args(RoleType)
