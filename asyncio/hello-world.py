#!/usr/bin/env python3

import asyncio

async def hello_world():
    print("Hello World!")

    await asyncio.sleep(1.0)
    print("Hello again!")


asyncio.run(hello_world())
