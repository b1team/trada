# trada
# [front end](https://github.com/b1team/vuewebchat)
## description
- The api for chat realtime
- Using FastApi, redis, websocket, mongodb
- Deploy with docker
# run local
### comment root_path in src/main.py
```
cp .env.template .env
poetry env use python3.x
poetry install
export PYTHONPATH=$PWD
poetry run python src/main.py
```
# run with docker
```
cp .env.template .env -> change DB to DB online
docker build --pull --rm -f "Dockerfile" -t trada:latest "."
docker-compose -f "docker-compose.yml" up -d --build
```
