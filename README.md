## Project setup

```
python -m pip install fastmcp
```

## Test project locally
```
fastmcp run main.py:mcp --transport http --port 8000
python client.py
```

## Deploy to live server
```
python -m pip install uv
uvx prefect-cloud login
uvx prefect-cloud github setup
uvx prefect-cloud deploy main.py:mcp --from gokula-krishna-dev/ai-engineering-session-4 --name hello --with fastmcp
uvx prefect-cloud run greet/hello
```