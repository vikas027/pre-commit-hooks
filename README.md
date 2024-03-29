pre-commit-hooks
================

Collection of pre-commit hooks

### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
---
repos:
-   repo: https://github.com/vikas027/pre-commit-hooks.git
    rev: master # Use the ref you want to point at, `master` is for testing
    hooks:
    - id: check-commitsar
    - id: present-files-dirs
      args: [--list, 'CHANGELOG.md,README.md,.github/PULL_REQUEST_TEMPLATE/pull_request_template.md']
```

### Hooks available

#### `check-commitsar`
Makes sure your commits are compliant with conventional commits using [commitsar](https://commitsar.aevea.ee/).

#### `present-files-dirs`
Check if the specified files and directories exists.
