"""Passthrough shim for OpenLineage extension."""
import sys

import structlog
from meltano.edk.logging import pass_through_logging_config
from openlineage_ext.extension import OpenLineage


def pass_through_cli() -> None:
    """Pass through CLI entry point."""
    pass_through_logging_config()
    ext = OpenLineage()
    ext.pass_through_invoker(
        structlog.getLogger("openlineage_invoker"),
        *sys.argv[1:] if len(sys.argv) > 1 else []
    )
