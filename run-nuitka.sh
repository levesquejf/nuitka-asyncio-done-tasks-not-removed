#!/usr/bin/env bash

docker build -t nuitka-asyncio-done-tasks-not-removed-nuitka -f Dockerfile-nuitka .
docker run -it --privileged nuitka-asyncio-done-tasks-not-removed-nuitka
