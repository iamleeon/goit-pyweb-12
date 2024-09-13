from fastapi import FastAPI

from src.routes import contacts

app = FastAPI(
    title="Contact Management API",
    description="API for managing contacts with CRUD operations.",
    version="1.0.0",
)

app.include_router(contacts.router, prefix='/api')


@app.get("/health", tags=["Health check"])
def health_check():
    return {"status": "healthy"}
