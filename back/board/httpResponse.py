from django.http import HttpResponse


class HttpError(Exception):
    def __init__(self, msg: str, status: int) -> None:
        self.msg = msg
        self.status = status

    def send(self):
        return HttpResponse(self.msg, status=self.status)
