import sys

if sys.version_info < (3, 8):  # pragma: no cover (<PY38)
    import importlib_metadata
else:  # pragma: no cover (PY38+)
    import importlib.metadata as importlib_metadata

CONFIG_FILE = '.pre-commit-config.yaml'
MANIFEST_FILE = '.pre-commit-hooks.yaml'

# Bump when installation changes in a backwards / forwards incompatible way
INSTALLED_STATE_VERSION = '1'
# Bump when modifying `empty_template`
LOCAL_REPO_VERSION = '1'

VERSION = importlib_metadata.version('pre_commit')

# `manual` is not invoked by any installed git hook.  See #719
STAGES = (
    'commit', 'merge-commit', 'prepare-commit-msg', 'commit-msg',
    'post-commit', 'manual', 'post-checkout', 'push',
)

DEFAULT = 'default'
