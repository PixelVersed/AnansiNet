# Environment

> This document explains how to set up a development environment for AnansiNet using either containers or a native installation.

## Development Container

An easy way to develop on Linux is by using containers.  
This project provides two container files: `Containerfile` and `Containerfile.debian`.

- `Containerfile` is based on **Alpine Linux** (≈ **1.64 GB**)
- `Containerfile.debian` is based on **Debian** (≈ **3.64 GB**)

Aside from the base image, there are no differences between them and both offer the same development environment. Choose whichever base you prefer.

To build and run the container, you can use **Podman**:

```sh
$ sudo podman build -t anansinet:1 .
$ sudo -E podman run --rm -it \
    --privileged --network=host \
    -v $PWD/AnansiNet:/src \
    -p 1420:1420 \
    --env DISPLAY \
    --env WAYLAND_DISPLAY \
    --env XDG_RUNTIME_DIR \
    -v $XDG_RUNTIME_DIR/$WAYLAND_DISPLAY:$XDG_RUNTIME_DIR/$WAYLAND_DISPLAY \
    anansinet:1
```

> `sudo` is required to access the host's network and scan connected devices.
> `-E` to [preserve environment variables](<https://wiki.archlinux.org/title/Running_GUI_applications_as_root#Using_sudo_-E>) else the UI will crash.

## Native Environment

### Windows

For native environemnt you need to install the following dependencies manually:

- [Tauri prerequisites](<https://tauri.app/start/prerequisites/>) (including [rust](<https://rust-lang.org/>))
- [python 3.13 or above](<https://www.python.org/downloads/>)
- [uv](<https://docs.astral.sh/uv/getting-started/installation/#standalone-installer>)
- [Bun](<https://bun.com/>)

### Linux

For Linux, the dependencies are the same as above, but make sure to install the `python3-dev` package instead of the standard `python3` package.

## Development

Running the app is simple:

```sh
$ cd /AnansiNet # /src if you're working inside a container
$ uv venv --python-preference only-system && source .venv/bin/activate
$ uv pip install --reinstall -e src-tauri/
$ bun tauri dev
```
