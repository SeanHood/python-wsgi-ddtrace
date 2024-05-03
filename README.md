# python-wsgi-ddtrace

Simple sample of using DataDog's `ddtrace` with a Flask App behind httpd with mod_wsgi because an example isn't in the docs.


```
docker compose up
curl localhost:8080
```

Lots of log output since `DD_TRACE_DEBUG=true`, you'll see the sample spans sent to `ddagent`
