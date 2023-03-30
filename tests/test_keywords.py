import pytest

from ai_ghostfunctions import keywords


@pytest.mark.parametrize(
    "kw,v",
    [
        (keywords.ASSISTANT, "assistant"),
        (keywords.USER, "user"),
        (keywords.SYSTEM, "system"),
        (keywords.CHAT_COMPLETION, "chat completion"),
        (keywords.COMPLETION, "completion"),
    ],
)
def test_keyword_value(kw: str, v: str) -> None:
    assert kw == v
