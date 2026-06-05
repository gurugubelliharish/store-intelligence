from fastapi import FastAPI
import json

app = FastAPI(
    title="Store Intelligence API",
    version="1.0"
)

# -----------------------------------
# Health Check
# -----------------------------------

@app.get("/")
def root():

    return {
        "message": "Store Intelligence API Running"
    }

# -----------------------------------
# Store Metrics
# -----------------------------------

@app.get("/metrics")
def get_metrics():

    with open(
        "backend/data/store_metrics.json",
        "r"
    ) as f:

        metrics = json.load(f)

    return metrics