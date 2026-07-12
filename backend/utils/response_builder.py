class ResponseBuilder:

    @staticmethod
    def success(
        message: str,
        data,
        processing_time: float,
    ):

        return {
            "success": True,
            "message": message,
            "data": data,
            "processing_time": processing_time,
        }

    @staticmethod
    def error(message: str):

        return {
            "success": False,
            "message": message,
            "data": None,
        }