from collections.abc import Generator
from typing import Any
from resonate import Resonate, Context, Yieldable
from threading import Event
# Connect to remote Resonate worker group
resonate = Resonate.remote(group="foo_nodes", host="http://localhost")

def foo(ctx: Context, identifier: str) -> Generator[Yieldable, Any, str]:
    result = yield ctx.run(bar, identifier)
    return result

# Simple helper function
def bar(ctx: Context, identifier: str) -> str:
    return f"id: {identifier}"

# Register the generator function
resonate.register(foo)

resonate.start()
print("worker running...")


try:
    Event().wait()
except KeyboardInterrupt:
    ...
