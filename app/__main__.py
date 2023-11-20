from app import create_app
import uvicorn

app = create_app()

if __name__ == "__main__":
    uvicorn.run("app:create_app", host="190.174.241.103", port=0, log_level="debug")

