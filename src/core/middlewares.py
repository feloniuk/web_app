import cProfile
import pstats
from datetime import datetime
from io import StringIO
from time import perf_counter

from django.conf import settings


class PerformanceMonitoringMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = perf_counter()
        pr = cProfile.Profile()
        pr.enable()
        response = self.get_response(request)
        pr.disable()
        s = StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
        ps.print_stats()
        finish = perf_counter()

        if finish - start > settings.MAX_RESPONSE_TIME:
            with open(f'{datetime.today().strftime("%Y-%m%-%d")}_performance', 'a') as f:
                f.write(f'URI: {request.path} \n')
                f.write(f'DEBUG INFO: {s.getvalue()} \n')
                f.write('_' * 20 + '\n')
                pass

        # Code to be executed for each request/response after
        # the view is called.

        return response
