"""Helpers for working with asyncio event loops in synchronous code."""

import asyncio


def get_or_create_event_loop() -> asyncio.AbstractEventLoop:
    """Return the current event loop or create one for the current thread."""

    try:
        loop = asyncio.get_event_loop()
        if loop.is_closed():
            raise RuntimeError
        return loop
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop