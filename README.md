# GutmanLabDockers
Creating Docker build scripts for various projects in my lab

To build docker image locally run (dont forget the period in the end)

```docker build -t dgutman/GutmanLabDockers:test .```

To get help on executing the docker container run

```docker run dgutman/GutmanLabDockers:test --help```

To list all CLIs encapsulated run

```docker run dgutman/GutmanLabDockers:test --list_cli```

To help on executing a CLI run

```docker run dgutman/GutmanLabDockers:test <cli-name> --help```

To actually run a CLI on local data run

```docker run -v local_dir:container_dir dgutman/GutmanLabDockers:test <cli-name> <args-needed-here>```
