import logging
from typing import Dict, List, Optional

from langkit.pattern_loader import PatternLoader
from whylogs.core.metrics.metrics import FrequentItemsMetric
from whylogs.core.resolvers import MetricSpec

from xleap.metrics.config import XleapMetricConfig, config
from xleap.metrics.core import register_metric

logger = logging.getLogger(__name__)

pattern_loader = PatternLoader()


def has_patterns(text):
    regex_groups = pattern_loader.get_regex_groups()
    if regex_groups:
        matched = None
        for group in regex_groups:
            for expression in group["expressions"]:
                if expression.search(text):
                    matched = matched or group["name"]
                    break
            if matched is not None:
                break

        return matched


def _wrapper(column):
    def wrappee(text):
        return [has_patterns(input) for input in text[column]]

    return wrappee


_registered: List[str] = []


def _unregister_metric_udf(old_name: str, namespace: Optional[str] = ""):
    from xleap.metrics.core import _multicolumn_udfs

    if _multicolumn_udfs is None or namespace not in _multicolumn_udfs:
        return

    _multicolumn_udfs[namespace] = [
        udf
        for udf in _multicolumn_udfs[namespace]
        if list(udf.udfs.keys())[0] != old_name
    ]


def _register_udfs(config: Optional[XleapMetricConfig] = config):
    from xleap.metrics.core import _resolver_specs

    global _registered
    if _registered and config is None:
        return

    default_metric_name = "has_patterns"
    pattern_metric_name = config.metric_name_map.get(
        default_metric_name, default_metric_name
    )

    for old in _registered:
        _unregister_metric_udf(old_name=old)
        if (
            _resolver_specs is not None
            and isinstance(_resolver_specs, Dict)
            and isinstance(_resolver_specs[""], List)
        ):
            _resolver_specs[""] = [
                spec for spec in _resolver_specs[""] if spec.column_name != old
            ]
    _registered = []

    if pattern_loader.get_regex_groups() is not None:
        for column in [config.prompt_column, config.response_column]:
            udf_name = f"{column}.{pattern_metric_name}"
            register_metric(
                [column],
                udf_name=udf_name,
                metrics=[MetricSpec(FrequentItemsMetric)],
            )(_wrapper(column))
            _registered.append(udf_name)


def init(
    pattern_file_path: Optional[str] = None,
    config: Optional[XleapMetricConfig] = config,
):
    if pattern_file_path:
        config.pattern_file_path = pattern_file_path

    global pattern_loader
    pattern_loader = PatternLoader(config)
    pattern_loader.update_patterns()

    _register_udfs(config)