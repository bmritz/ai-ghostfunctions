# How To

This section of the documentation contains common code snippets for common tasks with Ghostfunctions.

## Use a different OpenAI Model

By default, AI Ghostfunctions will use OpenAI's `gpt-4` model if the OpenAI API Key has access to it, optionally falling back to `gpt-3.5-turbo` if the API request fails with a `openai.InvalidRequestError`. You can configure the model to use `gpt-3.5-turbo` by default by using the `ai_callable` parameter on the `@ghostfunction` decorator:

```python
>>> def query_openai_35(**kwargs):
>>>     """Query OpenAI API with `query` and return the response."""
>>>     return openai.ChatCompletion.create(
>>>         model='gpt-3.5-turbo',
>>>         **kwargs
>>>     )
>>>
>>> @ghostfunction(ai_callable=query_openai_35)
>>> def complete_the_rhyme(phrase: str) -> str:
>>>     """Output a word that completes phrase with a rhyme."""
>>>
>>> complete_the_rhyme(phrase="If you blow a double bubble, you're sure to be in")
'trouble'
```

## Ensure deterministic results

One drawback of using ghostfunctions is that the same inputs to a ghostfunction may return different outputs, [even when temperature is set to 0](https://community.openai.com/t/a-question-on-determinism/8185/2). To keep the library small and focused, and to give users flexibility in caching configurations, I recommend using a caching decorator to ensure determinism. One simple, built-in caching mechanism is [`functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache):

```python
>>> from functools import lru_cache
>>>
>>> @lru_cache
>>> @ghostfunction(ai_callable=query_openai_35)
>>> def chaos(seed: int) -> str:
>>>     """Returns chaos!!!"""
>>>
>>> chaos(seed=1)
'chaos!!!'
>>> chaos(seed=2)
'Chaos!!!'
>>> chaos(seed=1)
'chaos!!!'
>>> chaos(seed=2)
'Chaos!!!'
```

The [`cachetools`](https://cachetools.readthedocs.io/en/latest/]) third-party library also contains other implementations of caching decorators.
