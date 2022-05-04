# DuckDuck
A async wrapper for the RandomDuck API

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
  url = await client.fetch_random()
  print(url)

asyncio.run(main())
```

## SUPPORT
Contact me: iamSkev#4260
