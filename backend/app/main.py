from fastapi import FastAPI

app = FastAPI(title="ClearSOC Backend")

@app.get("/")
def root():
    return {"message": "ClearSOC backend is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}