# asynchronous-programming-in-python

## Concurrency Types

### Pre-emptive multitasking (threading)

The operating system decides when to switch tasks external to Python. Only one processor.

### Cooperative multitasking (asyncio)

The tasks decide when to give up control. Only one processor.

### Multiprocessing

The processes all run at the same time on different processors. Many processors.

## Process Types

### I/O-Bound Process

Your program spends most of its time talking to a slow device, like a network connection, a hard drive, or a printer.
Speeding it up involves overlapping the times spent waiting for these devices.

### CPU-Bound Process

You program spends most of its time doing CPU operations.
Speeding it up involves finding ways to do more computations in the same amount of time.

