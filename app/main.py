from fastapi import FastAPI
from app.api.v1.auth import auth
import uvicorn
import signal
import sys


app = FastAPI(
    title="Ecom auth",
    description="Ecommerce user authentication apis"

)

def signal_handler(sig, frame):
    print("Gracefully shutting down...")
    sys.exit(0)

# Register the signal handler for SIGINT (Ctrl + C)
signal.signal(signal.SIGINT, signal_handler)


app.include_router(auth)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)