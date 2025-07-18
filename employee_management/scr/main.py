from fastapi import FastAPI
from uvicorn import run
from scr.routes.all_routes import router
from scr.db.models import init_db

app = FastAPI(title="Employee Management System")


@app.on_event("startup")
async def init_process():
    init_db()


app.include_router(router)

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=12000, reload=True)