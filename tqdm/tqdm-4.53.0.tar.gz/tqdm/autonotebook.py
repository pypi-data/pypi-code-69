"""
Automatically choose between `tqdm.notebook` and `tqdm.std`.

Usage:
>>> from tqdm.autonotebook import trange, tqdm
>>> for i in trange(10):
...     ...
"""
import os
import sys

try:
    get_ipython = sys.modules['IPython'].get_ipython
    if 'IPKernelApp' not in get_ipython().config:  # pragma: no cover
        raise ImportError("console")
    if 'VSCODE_PID' in os.environ:  # pragma: no cover
        raise ImportError("vscode")
except:
    from .std import tqdm, trange
else:  # pragma: no cover
    from .notebook import tqdm, trange
    from .std import TqdmExperimentalWarning
    from warnings import warn
    warn("Using `tqdm.autonotebook.tqdm` in notebook mode."
         " Use `tqdm.tqdm` instead to force console mode"
         " (e.g. in jupyter console)", TqdmExperimentalWarning, stacklevel=2)
__all__ = ["tqdm", "trange"]
