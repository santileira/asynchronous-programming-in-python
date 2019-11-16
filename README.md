# asynchronous-programming-in-python

## Concurrency Types

### Pre-emptive multitasking (threading)

The operating system decides when to switch tasks external to Python. Only one processor.

### Cooperative multitasking (asyncio)

The tasks decide when to give up control. Only one processor.

### Multiprocessing

The processes all run at the same time on different processors. Many processors.

