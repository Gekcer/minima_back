from fastapi import FastAPI
from start_center import start_center

app = FastAPI()

app.include_router(start_center.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True, port=3333)