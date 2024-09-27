"""Prometheus metrics instrumentation functions.

Additional functions to collect and set Prometheus metrics for RAM and CPU.
"""

from typing import Callable

import psutil
from prometheus_client import Gauge
from prometheus_fastapi_instrumentator.metrics import Info


def ram_usage(
    metric_name: str = "memory_usage_bytes",
    metric_doc: str = "Memory usage in bytes.",
    metric_namespace: str = "",
    metric_subsystem: str = "",
) -> Callable[[Info], None]:
    """Create a Prometheus gauge for RAM usage.

    This function initializes a Prometheus Gauge metric to track RAM usage
    percentage. It defines an instrumentation function that collects
    virtual memory and swap memory usage statistics using the psutil
    library and sets the corresponding values in the gauge.

    Returns:
        Callable[[Info], None]: The instrumentation function to collect
        and set RAM usage metrics.
    """
    ram_metric = Gauge(
        name=metric_name,
        documentation=metric_doc,
        labelnames=("type", "status"),
        namespace=metric_namespace,
        subsystem=metric_subsystem,
    )

    def instrumentation(info: Info) -> None:
        ram = psutil.virtual_memory()
        swap = psutil.swap_memory()

        ram_metric.labels(type="virtual", status="").set(ram.used)
        ram_metric.labels(type="virtual", status="cached").set(ram.cached)
        ram_metric.labels(type="swap", status="").set(swap.used)

    return instrumentation


def cpu_usage(
    metric_name: str = "cpu_usage_percent",
    metric_doc: str = "CPU usage percent.",
    metric_namespace: str = "",
    metric_subsystem: str = "",
) -> Callable[[Info], None]:
    """Create a Prometheus gauge for CPU usage.

    This function initializes a Prometheus Gauge metric to track CPU usage
    percentage. It defines an instrumentation function that collects CPU
    usage statistics for each core using the psutil library and sets the
    corresponding values in the gauge.

    Returns:
        Callable[[Info], None]: The instrumentation function to collect
        and set CPU usage metrics.
    """
    cpu_metric = Gauge(
        name=metric_name,
        documentation=metric_doc,
        labelnames=("core",),
        namespace=metric_namespace,
        subsystem=metric_subsystem,
    )

    def instrumentation(info: Info) -> None:
        for c, p in enumerate(psutil.cpu_percent(interval=1, percpu=True)):
            cpu_metric.labels(core=c).set(p)

    return instrumentation
