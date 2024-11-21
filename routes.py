# Importing Dependencies
from fastapi import FastAPI

from api.tagging import router as tagging_router

# Create FastAPI instance
app = FastAPI()

# Include Routers
app.include_router(tagging_router)

# Health Check
@app.get("/ready")
async def ready():
    return {"status": "Server is up and running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("routes:app", host="0.0.0.0", port=8000, reload=True)