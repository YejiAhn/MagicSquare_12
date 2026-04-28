"""Domain and validation errors (PRD-aligned codes)."""


class ValidationError(Exception):
    """Input / shape contract violation before domain solve."""

    def __init__(self, code: str, message: str = "") -> None:
        self.code = code
        self.message = message or code
        super().__init__(self.message)


class DomainError(Exception):
    """Valid-shaped input but no valid placement (or other domain rule)."""

    def __init__(self, code: str, message: str = "") -> None:
        self.code = code
        self.message = message or code
        super().__init__(self.message)
