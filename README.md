# gutmanlabdocks
Creating Docker build scripts for various projects in my lab

To build docker image locally run (dont forget the period in the end)

```docker build -t dgutman/gutmanlabdockers:test .```

To get help on executing the docker container run

```docker run dgutman/gutmanlabdockers:test --help```

To list all CLIs encapsulated run

```docker run dgutman/gutmanlabdockers:test --list_cli```

To help on executing a CLI run

```docker run dgutman/gutmanlabdockers:test <cli-name> --help```

To actually run a CLI on local data run

```docker run -v local_dir:container_dir dgutman/gutmanlabdockers:test <cli-name> <args-needed-here>```
