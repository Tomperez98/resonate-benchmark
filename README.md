## Start server
```bash
make serve WORKERS=1 # configure number of workers
```

## Start webserver
```bash
cd ts && bun client.ts
cd py && uv run client.py
```

## Start n-workers
```bash
cd ts && bun worker.ts
cd py && uv run worker.py
```
