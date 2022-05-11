# DuckDuck
A async wrapper for the RandomDuck API

[![Documentation Status](https://readthedocs.org/projects/duckduck/badge/?version=latest)](https://duckduck.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/duckduck)](https://pypi.org/project/duckduck/)

## Features
- An async library.
- Has all of the endpoints covered in v2.
- Has a object oriented design so it's easy to use.

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

## Support
Contact me: [iamSkev#4260](https://discord.com/users/381799048228896788)
