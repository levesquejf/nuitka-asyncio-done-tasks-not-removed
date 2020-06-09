#!/usr/bin/env bash

docker build -t nuitka-asyncio-done-tasks-not-removed-native -f Dockerfile-native .
docker run -it --privileged nuitka-asyncio-done-tasks-not-removed-native
