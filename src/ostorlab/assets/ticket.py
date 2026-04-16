"""Report asset."""

import dataclasses
from typing import Optional, List

from ostorlab.assets import asset


@dataclasses.dataclass
class Tag:
    """Tag message."""

    name: Optional[str] = None
    value: Optional[str] = None


@dataclasses.dataclass
@asset.selector("v3.report.ticket")
class Ticket(asset.Asset):
    """Ticket asset."""

    title: str
    ticket_id: Optional[str] = None
    description: Optional[str] = None
    tags: List[Tag] = dataclasses.field(default_factory=list)
    assigned_user: Optional[str] = None

    def __str__(self) -> str:
        return f"Ticket {self.title}"

    @property
    def proto_field(self) -> str:
        return "ticket"
