from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.core.config import settings
from src.api.v1.routes import messages_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan, title="Registry API")

app.include_router(messages_router)


@app.get('/api/health')
def health_check():
    return "OK"


if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.APP_HOST, port=settings.APP_PORT, reload=settings.APP_DEBUG_MODE)
