Issue tracked at [Nuitka/#748](https://github.com/Nuitka/Nuitka/issues/748).

This repo reproduces a bug causing asyncio tasks leaks when using `Websockets` and `Nuitka`. The reproducer uses Docker and Iptables to simulate connection failure which causes the tasks to stay in `asyncio.Task.all_tasks()`.

This bug is present with Python 3.8.3 and Nuitka 0.6.8.3.

To test with Python: `./run-native.sh`.

To test with Nuitka: `./run-nuitka.sh`.

After a few hours, some `done` tasks stay in the `asyncio.Task.all_tasks()` when compiled with Nuitka which is not the case with Python. It usually takes a few minutes to clear on Python.
