from fastapi import FastAPI
from celery_worker import create_task
from data import database, models

app = FastAPI()
db = database.SessionLocal()


@app.get("/")
async def root():
    records = db.query(models.Record).all()
    create_task.delay()
    return {"records": records}


@app.get("/chart")
async def view_chart():
    # Retrieve plotly chart as image
    return {"image": ""}
