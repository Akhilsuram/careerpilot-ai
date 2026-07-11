class CareerPilotException(Exception):
    """Base exception for CareerPilot AI."""
    pass


# ==================================
# Resume
# ==================================

class ResumeParsingException(CareerPilotException):
    pass


# ==================================
# Database
# ==================================

class DatabaseException(CareerPilotException):
    pass


# ==================================
# Provider
# ==================================

class ProviderException(CareerPilotException):
    pass


class ProviderUnavailableException(ProviderException):
    pass


class ProviderTimeoutException(ProviderException):
    pass


class ProviderAuthenticationException(ProviderException):
    pass


# ==================================
# Jobs
# ==================================

class JobSearchException(CareerPilotException):
    pass


# ==================================
# Validation
# ==================================

class ValidationException(CareerPilotException):
    pass