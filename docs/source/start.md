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
  asyncio.get_running_loop().set_exception_handler(lambda loop, context: None) # This suppresses the warning that comes from the aiohttp library you can remove this line if you want the warnings to be in your terminal.
  url = await client.fetch_random()
  print(url)

asyncio.run(main())
```
