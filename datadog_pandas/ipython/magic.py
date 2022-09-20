from IPython.core.magic import (magics_class, cell_magic, line_magic, Magics)
from IPython.core import magic_arguments

from datadog_pandas import query


@magics_class
class DatadogMetricsMagics(Magics):
    @magic_arguments.magic_arguments()
    @magic_arguments.argument('api_key', help='Datadog API Key')
    @magic_arguments.argument('app_key', help='Datadog App Key')
    @line_magic
    def datadog_connect(self, line):
        args = magic_arguments.parse_argstring(self.datadog_connect, line)
        self.dd = query.DatadogMetrics({
            'api_key': args.api_key,
            'app_key': args.app_key,
        })

    @magic_arguments.magic_arguments()
    @magic_arguments.argument('start', help='Start timestamp')
    @magic_arguments.argument('end', help='End timestamp')
    @magic_arguments.argument('output', nargs='?', help='Output variable')
    @cell_magic
    def datadog_query(self, line, cell):
        args = magic_arguments.parse_argstring(self.datadog_query, line)
        result = self.dd.query(cell, start=args.start, end=args.end)

        if args.output:
            self.shell.user_ns[args.output] = result
        else:
            return result


ip = get_ipython()
ip.register_magics(DatadogMetricsMagics)
