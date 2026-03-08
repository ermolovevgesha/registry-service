from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)


if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.APP_HOST, port=settings.APP_PORT, reload=settings.APP_DEBUG_MODE)
