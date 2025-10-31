## Project setup

```
conda create -n session-4
conda activate session-4
conda install python=3.14 
python -m pip install fastmcp
```

## Test project locally
```
fastmcp run main.py:mcp --transport http --port 8000
python client.py
```