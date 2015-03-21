# 500
500 Card Game

## Installation

The server application is written with the Tornado web framework, so it is required to install that first. This is easily done in a virtualenv.

```pip install tornado```

Then copy the sample config file to config.ini and create your own secret key, this can be anything as long as people can't guess it.

```cp sample_config.ini config.ini```

Then you are good to go!
```python server.py```

Connect to localhost:8888 or your.ip.address:8888 .
