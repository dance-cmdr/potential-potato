# potential-potato

This is a boilerplate to start python script projects.

It contains a number of tools I find important for a basic Developer Experience and I definetely recomend everyone to check out or find their own alternatives.

[See the pipfile dev dependencies for more information](./Pipfile)

## Quick Start

```shell
pipenv install --dev
pipenv shell
```

### Enable pre-commit hooks

```shell
    pre-commit install --hook-type pre-commit --hook-type pre-push --hook-type commit-msg
```

### To run tests while you develop

```shell
ptw tests/ src/
```

## Contributing

### Commiting Changes

As a best practice we are using conventional commits e.g `feat(DX):initialise repo`.

To enforce the patter we use commitizen. A commit message helper is available through commitizen.

```
cz commit
```

If you prefer to use the git interface e.g. `git commit -m "add(dx):message"` and you have pre-commit hooks installed. Your commit message will be linted with `cz check`

## Version Tagging

We are following Semver version convention e.g. v0.0.1.

To bump the a version use the commitizen interface

```shell
cz bump
```
