from fastapi import FastAPI
from app.api.routes_v3 import router_v3
from app.api.routes_v4 import router_v4
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Angular URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_v3, prefix="/v3/api")
app.include_router(router_v4, prefix="/v4/api")


@app.get("/")
def root():
    return {"message": "API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)