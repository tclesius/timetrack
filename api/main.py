from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.user.view import router as user_router
from api.log.view import router as log_router
from api.auth.view import router as auth_router
from api.chip.view import router as chip_router

app = FastAPI()

app.include_router(user_router)
app.include_router(log_router)
app.include_router(auth_router)
app.include_router(chip_router)

origins = [
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Service healthy."}
