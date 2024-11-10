#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:08:49 2023

@author: user
"""

import asyncio
from random import randint
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send('[' + str(randint(1, 10)) + '] ' + message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
