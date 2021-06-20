import uvicorn


if __name__ == "__main__":
    options = {
        "host": "0.0.0.0",
        "port": 9999,
        "log_level": "info",
        "reload": True,
        "root_path": "/api"
    }
    uvicorn.run("src.api.app:app", **options)
