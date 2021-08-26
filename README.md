
# inventory-backend

Ultimate product catalog

![main-structure](https://user-images.githubusercontent.com/20068601/130909583-1ef67788-eefd-4a23-98c1-29b46b87f45a.png)

## Packages

We are using [pip-tools](https://github.com/jazzband/pip-tools) here.


For first install run:
```
pip install -r requirements.txt 
```

Add new packages and their versions only to `requirements.in`. Then:

* to update all dependencies (within specified versions in `requirements.in`)
```
pip-compile -U
```

* to update single package
```
pip-compile -P some-package
```

After that you may want to sync packages locally by running:
```
pip-sync
```

## Testing

Make sure you prepared database for tests. You may run `docker-compose up -d` to deploy necessary resourses.

Enter `pytest` to run your tests inside your environment.

Put your tests in corresponding django app folder. 

## Linting

Please run `isort . && black . && flake8` before subbmiting your work.

