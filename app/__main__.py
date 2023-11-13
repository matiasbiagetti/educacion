from app import create_app
import uvicorn

app = create_app()

if __name__ == "__main__":
    uvicorn.run("app:create_app", host="0.0.0.0", port=4567, log_level="debug")

