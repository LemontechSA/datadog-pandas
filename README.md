# Datadog Pandas

Python library for querying Datadog and accessing the results as
 [Pandas](https://pandas.pydata.org/) data structures.

This is mostly intended for use in [Jupyter](https://jupyter.org/) notebooks.

## Example

Evaluate an instant query at a single point in time:

```python
>>> from datadog_pandas import query
>>>
>>> dd_options = {"api_key": "XXX", "app_key": "XXX"}
>>> p = query.DatadogMetrics(dd_options)
>>> p.query('sum:caseflow.ct.attachments.requests{*}.rollup(sum, 86400)', '2020-05-10T00:00:00Z', '2020-05-12T00:00:00Z')
```

## Installation

Latest release via [`pip`](https://pip.pypa.io):

```bash
pip install datadog-pandas [--user]
```

via Git:

```bash
git clone https://github.com/LemontechSA/datadog-pandas.git; cd datadog-pandas
python3 setup.py install [--user]
```

## Licence

Licenced under the [MIT License](https://choosealicense.com/licenses/mit/). See `LICENSE` for details.
