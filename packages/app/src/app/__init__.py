import uvicorn
import time


def main() -> None:
    print("Setting up uvicorn server...")
    time.sleep(5)
    uvicorn.run("app.app:app", reload=True)
