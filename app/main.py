import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from module.services.routers import process_router


app = FastAPI(
    title="Dhruva ProcessMaster",
    description="Backend API for Preprocessing and PostProcessing of ML models",
)

app.include_router(process_router.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5050, log_level="info", workers=2)