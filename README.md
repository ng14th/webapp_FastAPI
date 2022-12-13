 
# STEP 1 :
## Do this one time when you clone source
 - THIS PROJECT USING POETRY TO MANAGE LIBRARY
- Install poetry, require python version >= 3.10
 ```
    curl -sSL https://install.python-poetry.org | python3.10 -
 ```
- Config poetry to create env 
```
    $ chmod +x ./scripts/*.sh
    $ ./scripts/initialize_project.sh
```
# STEP 2 :
## If you done Step 1 
- Activate venv poetry :
```
    $ source .venv/bin/activate
```
- Run App
```
    $ ./scripts/run_app.sh
```
## For install new libary 
- Use method add of poetry
```
    $ poetry add "lib"
    Example
    $ poetry add socketio
```

# AFTER RUN APP
- Access http://172.27.230.25:8000/
```
    If see {"message":"Hello World"} --> correct 
```
- Access http://172.27.230.25:8000/docs 
```
    See all method of project 
```
