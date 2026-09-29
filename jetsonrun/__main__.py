"""Entry point for ``python -m jetsonrun``."""

from __future__ import annotations

import sys

from jetsonrun.cli import main

if __name__ == "__main__":
    sys.exit(main())
