* Hello bro.
These are unix commands im too lazy to find windows ones
change the directory names to your liking ig, but the venv one should stay the same please
```
❯ git clone https://github.com/twistedttea/stroll webproj && cd ./webproj
❯ mkdir env_webproject && python3 -m venv env_webproject && source env_webproject/bin/activate
```
For testing run something like
```
❯ python manage.py runserver 0.0.0.0:8000
```
