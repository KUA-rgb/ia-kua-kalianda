from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import nikah, cerai, rujuk, stats

app = FastAPI(
    title="IA KUA Kalianda",
    description="Integrated Application untuk Kantor Urusan Agama (KUA) Kalianda",
    version="1.0.0",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(nikah.router)
app.include_router(cerai.router)
app.include_router(rujuk.router)
app.include_router(stats.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to IA KUA Kalianda API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/api/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
