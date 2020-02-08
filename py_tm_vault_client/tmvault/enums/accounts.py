from enum import Enum


class AccountStatus(Enum):
    """Enumeration for the status of an account.

    - :ACCOUNT_STATUS_UNKNOWN:
    - :ACCOUNT_STATUS_OPEN:
    - :ACCOUNT_STATUS_CANCELLED:
    - :ACCOUNT_STATUS_PENDING_CLOSURE:
    - :ACCOUNT_STATUS_PENDING:
    """
    ACCOUNT_STATUS_UNKNOWN = 'ACCOUNT_STATUS_UNKNOWN'
    ACCOUNT_STATUS_OPEN = 'ACCOUNT_STATUS_OPEN'
    ACCOUNT_STATUS_CLOSED = 'ACCOUNT_STATUS_CLOSED'
    ACCOUNT_STATUS_CANCELLED = 'ACCOUNT_STATUS_CANCELLED'
    ACCOUNT_STATUS_PENDING_CLOSURE = 'ACCOUNT_STATUS_PENDING_CLOSURE'
    ACCOUNT_STATUS_PENDING = 'ACCOUNT_STATUS_PENDING'
