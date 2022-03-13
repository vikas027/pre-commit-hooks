pre-commit-hooks
================

Collection of pre-commit hooks

### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/vikas027/pre-commit-hooks.git
    rev: master # Use the ref you want to point at, `master` is for testing
    hooks:
    -   id: commitsar-check
```

### Hooks available

#### `commitsar-check`
Makes sure your commits are compliant with conventional commits using [commitsar](https://commitsar.aevea.ee/).
