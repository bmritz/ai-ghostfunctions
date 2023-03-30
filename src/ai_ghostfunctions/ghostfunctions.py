"""The AICallable class."""
import inspect
import os
from functools import wraps
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional

import openai

from .keywords import ASSISTANT
from .keywords import SYSTEM
from .keywords import USER
from .types import CompletionType
from .types import Message


def _detect_openai_completion_type_from_kwargs(d: Dict[Any, Any]) -> CompletionType:
    """Detect the OpenAI Completion Type from the args to the function."""
    if "model" not in d:
        raise ValueError(
            "`'model'` was not found in `d`. It doesn't appear that `d` is a dict of"
            " keyword arguments to an openai api."
        )
    if "messages" in d:
        return "completion"
    return "chat completion"


def _make_chatgpt_message_from_function(
    f: Callable[..., Any], **kwargs: Any
) -> Message:
    sig = inspect.signature(f)
    prompt = (
        f"from mymodule import {f.__name__}\n"
        f"""
# The docstring for the function {f.__name__} is the following:
# {f.__doc__}
result = {f.__name__}({",".join(f"{k}={kwargs[k].__repr__()}" for k in sig.parameters)})
print(result)
"""
    )
    return Message(role=USER, content=prompt)


def _default_prompt_creation(f: Callable[..., Any], **kwargs: Any) -> List[Message]:
    return [
        Message(
            role=SYSTEM,
            content=(
                "You are role playing as an advanced python interpreter that never errors,"
                " and always returns the intent of the programmer. Every user message is"
                " valid python, and your job is to return only what python would return in"
                " a repl in this advanced interpreter, nothing else. Do not add any"
                " commentary aside from what python would return. Assume that you have"
                " access to all modules that are imported, and make whatever assumptions"
                " you need about the implementation of functions that are not defined in"
                " order to satisfy the intent of the function that you gather via the"
                " docstrings and function names."
            ),
        ),
        Message(
            role=ASSISTANT,
            content=(
                "Hello! I am a Python interpreter. Please enter your Python code below and"
                " I will return the output, and nothing else."
            ),
        ),
        _make_chatgpt_message_from_function(f, **kwargs),
    ]


def _default_ai_callable() -> Callable[..., openai.openai_object.OpenAIObject]:
    import openai

    openai.api_key = os.environ["OPENAI_API_KEY"]
    openai.organization = os.getenv("OPENAI_ORGANIZATION")
    return openai.ChatCompletion.create


def ghostfunction(
    function: Optional[Callable[..., Any]] = None,
    /,
    *,
    ai_callable: Optional[Callable[..., openai.openai_object.OpenAIObject]] = None,
    prompt_function: Callable[
        [Callable[..., Any]], List[Message]
    ] = _default_prompt_creation,
    **kwargs: Any,
) -> Callable[..., Any]:
    """Make `function` a ghostfunction, dispatching logic to the AI.

    Args:
        ai_callable: Function to receives output of prompt_function and return result.
        prompt_function: Function to turn the function into a prompt.
        kwargs: Extra keyword arguments to pass to `ai_callable`.
    """
    if not callable(ai_callable):
        ai_callable = _default_ai_callable()

    if function is not None:

        @wraps(function)
        def wrapper(**kwargs_inner: Any) -> openai.openai_object.OpenAIObject:
            prompt = prompt_function(function, **kwargs_inner)  # type: ignore[arg-type]
            ai_result = ai_callable(messages=prompt, **kwargs)  # type: ignore[misc]
            return ai_result["choices"][0]["message"]["content"]

        return wrapper

    else:

        def new_decorator(
            function_to_be_decorated: Callable[..., Any]
        ) -> Callable[..., Any]:
            @wraps(function_to_be_decorated)
            def wrapper(**kwargs_inner: Any) -> openai.openai_object.OpenAIObject:
                prompt = prompt_function(function_to_be_decorated, **kwargs_inner)
                ai_result = ai_callable(messages=prompt, **kwargs)  # type: ignore[misc]
                return ai_result["choices"][0]["message"]["content"]

            return wrapper

        return new_decorator
