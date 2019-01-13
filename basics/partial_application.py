#!/usr/bin/env python3

import functools

def log(message, subsystem):
    print(f"{subsystem}: {message}")

server_log = functools.partial(log, subsystem='server')
server_log('Unable to open socket')
