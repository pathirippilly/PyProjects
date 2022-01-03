import datetime
from argparse import ArgumentParser
import pytz


class Job:
    def __init__(self, *args, time_zone='utc', log_metrics: bool = True, **kwargs):
        self._tz = pytz.timezone(time_zone)
        self._known, self._unknown = self.setup_args().parse_known_args()
        self.default_mode = self._known.mode
        self.app_name = self._known.app
        self.emails = self._known.emails
        self.args = args
        self.log_metrics = log_metrics

    def setup_args(self) -> None:
        self.args_parser = ArgumentParser()
        self.args_parser.add_argument('-app', '--app_name', dest='app',
                                      default=f"python_job_{datetime.datetime.now(self._tz)}",
                                      help="python application name.Default value is python_job_<current time for "
                                           "mentioned time zone>")
        self.args_parser.add_argument('-m', '--mode', dest='mode', default='DAILY',
                                      help="Execution mode.(i.e, DAILY,HISTORY,RERUN or TEST)")
        self.args_parser.add_argument('-e', '--emails', dest='emails', default='',
                                      help="List of status emails separated by comma.Default is an empty string")
