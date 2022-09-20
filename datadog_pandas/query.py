import datetime
from typing import Union
from datadog import initialize, api

import numpy as np
import pandas as pd

Timestamp = Union[str, float, datetime.datetime]  # RFC-3339 string or as a Unix timestamp in seconds
Matrix = pd.DataFrame


class DatadogMetrics:
    def __init__(self, dd_options):
        """
        Initialize Datadog client.

        :param dd_options: Datadog client options params.
        """
        initialize(**dd_options)

    def __enter__(self):
        return self

    def query(self, query: str, start: Timestamp, end: Timestamp) -> Matrix:
        """
        Evaluates an instant query at a single point in time.

        :param query: Datadog expression query string.
        :param start: Evaluation timestamp.
        :param end: Evaluation timestamp.
        """

        response = api.Metric.query(
            start=_timestamp(start),
            end=_timestamp(end),
            query=query
        )

        return to_pandas(response)


def to_pandas(data: dict) -> Matrix:
    """Convert Datadog data object to Pandas object."""
    return pd.DataFrame({
        r['metric']:
            pd.Series((np.float64(v[1]) for v in r['pointlist']),
                        index=(pd.Timestamp(v[0]/1000, unit='s') for v in r['pointlist']))
        for r in data['series']})


def _timestamp(value):
    if isinstance(value, datetime.datetime):
        return value.timestamp()
    else:
        return datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S').timestamp()
