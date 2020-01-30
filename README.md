## aioworker

A Python worker running over `asyncio`

### Requirements

python 3.7+, aiotools==0.8.5

### Usage

```python
import asyncio

from aioworker import Service, Worker

async def task_1(loop):
    while True:
        print('Hello world')
        await asyncio.sleep(2)


if __name__ == '__main__':
    #  Run the server using 1 worker processes.
    Service(Worker(
        tasks=[task_1],
    )).run(num_workers=1)
```

or run tasks and the webserver

```python
import asyncio

from aioworker import Service, Worker


async def sleeping(loop):
    while True:
        print('Sleeping for 2 seconds...')
        await asyncio.sleep(2)


async def on_client_connect(reader, writer):
    """
    Read up tp 300 bytes of TCP. This could be parsed usign the HTTP protocol for example
    """
    data = await reader.read(300)
    print(f'TCP Server data received: {data} \n')
    writer.write(data)
    await writer.drain()
    writer.close()


if __name__ == '__main__':
    # Run the server using 1 worker processes.
    Service(Worker(
        tasks=[sleeping],
        web_server_config={
            'client_connected_cb': on_client_connect,
        },
    )).run(num_workers=1)

```

## How to stop the worker:

`ctrl+c`

## Default values:

| Variable | Default |
|----------|---------|
| TCP server host| 0.0.0.0|
| TPC server port | 8888 |
