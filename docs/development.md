# environment

## dev container

an easy way to develop on linux is using containers

```sh
$ podman build -t anansinet:1 .
$ podman run --rm -it -v $PWD/anansinet:/src -p 1420:1420 --env DISPLAY --env WAYLAND_DISPLAY --env XDG_RUNTIME_DIR -v $XDG_RUNTIME_DIR/$WAYLAND_DISPLAY:$
XDG_RUNTIME_DIR/$WAYLAND_DISPLAY anansinet:1
```

## native

For native environemnt you need to install the following dependencies manually:

- [Tauri prerequisites](<https://tauri.app/start/prerequisites/>) (including [rust](<https://rust-lang.org/>))
- [python 3.13 or above](<https://www.python.org/downloads/>)
- [Bun](<https://bun.com/>)

# development

running the app is super simple:

```sh
$ cd /anansinet # /src if you're working inside a container
$ bun install && bun run tauri dev
```
