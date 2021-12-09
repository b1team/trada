# trada
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
cp .env.template .env
docker build --pull --rm -f "Dockerfile" -t trada:latest "."
docker-compose -f "docker-compose.yml" up -d --build
```
# front end ````https://github.com/b1team/vuewebchat````
