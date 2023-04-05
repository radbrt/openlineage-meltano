"""Passthrough shim for MeltanoLineage extension."""
import sys

import structlog
from meltano.edk.logging import pass_through_logging_config
from meltanolineage_ext.extension import MeltanoLineage


def pass_through_cli() -> None:
    """Pass through CLI entry point."""
    pass_through_logging_config()
    ext = MeltanoLineage()
    ext.pass_through_invoker(
        structlog.getLogger("meltanolineage_invoker"),
        *sys.argv[1:] if len(sys.argv) > 1 else []
    )
