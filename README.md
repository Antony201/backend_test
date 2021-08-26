
# inventory-backend

Ultimate product catalog

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
