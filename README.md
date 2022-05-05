# DuckDuck
A async wrapper for the RandomDuck API

[![PyPI](https://img.shields.io/pypi/v/duckduck)](https://pypi.org/project/duckduck/)

## FEATURES
- An async library.
- Has all of the endpoints covered in v2.
- Has a object oriented design so it's easy to use.

## INSTALLATION
```bash
$python -m pip install DuckDuck
```

## EXAMPLE
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

## SUPPORT
Contact me: [iamSkev#4260](https://discord.com/users/381799048228896788)
