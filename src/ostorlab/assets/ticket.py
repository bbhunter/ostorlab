"""Report asset."""

import dataclasses
from typing import Optional

from ostorlab.assets import asset


@dataclasses.dataclass
class Comment:
    """Comment message."""

    author: Optional[str] = None
    value: Optional[str] = None


@dataclasses.dataclass
@asset.selector("v3.report.ticket")
class Ticket(asset.Asset):
    """Ticket asset."""

    title: str
    ticket_id: Optional[str] = None
    description: Optional[str] = None
    comments: list[Comment] = dataclasses.field(default_factory=list)
    assigned_user: Optional[str] = None

    def __str__(self) -> str:
        return f"Ticket {self.title}"

    @property
    def proto_field(self) -> str:
        return "ticket"
