# Hello bro.
## Instructions
This requires [Docker](https://docs.docker.com/compose/install/)

This also requires an .env file, which is purposefully ignored in every commit. \
**Please** do not force it in, just grab it from the discord on first clone and you should be good to go.

While inside of the root of the project, for initial run please ->
``` sh
docker compose up -d --build
```

To stop the server (if it's a daemon)
``` sh
docker compose down
```

## In the event of a build failure, please hit me up, maybe try these.

This deletes the created volumes, WILL WIPE LOCAL DB 
``` sh
docker compose down -v
```

You can also get rid of the -d option when you are debugging for more verbosity
