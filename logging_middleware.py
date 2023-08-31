import logging

logger = logging.getLogger(__name__)

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def _call__(self, request):
        # логируем информацию о входящем запросе
        logger.info("Request: %s, %s", response.method, request.path)

        response = self.get_response(request)

        # Логируем информацию о исходящем ответе
        logger.info("Rsponse: %S", response.status_code)
        return response
