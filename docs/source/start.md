# Getting Started
[![PyPI](https://img.shields.io/pypi/v/duckduck)](https://pypi.org/project/duckduck/)

## Installation
```bash
$python -m pip install DuckDuck
```

## Example
```py
import asyncio

import DuckDuck

client = DuckDuck.Duck()

async def main():
  url = await client.fetch_random()
  print(url)

asyncio.run(main())
```
