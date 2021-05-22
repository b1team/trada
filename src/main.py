import uvicorn


if __name__ == "__main__":
    options = {
        "host": "0.0.0.0",
        "port": 9000,
        "log_level": "info",
        "reload": True,
    }
    uvicorn.run("src.api.app:app", **options)
