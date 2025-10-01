from datetime import datetime
from fastapi import Request
from resonate import Resonate
from fastapi import FastAPI
from uuid import uuid4
import asyncio
import uvloop
import uvicorn

resonate = Resonate.remote(host="http://localhost")

app = FastAPI()

@app.get("/")
async def _(req: Request):
    identifier = str(uuid4())
    result = await resonate.options(target="poll://any@foo_nodes").begin_rpc(identifier, "foo", identifier)
    return {"time": datetime.now().isoformat(), "meesage":result}


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
uvicorn.run(app, host="0.0.0.0", port=8081)
