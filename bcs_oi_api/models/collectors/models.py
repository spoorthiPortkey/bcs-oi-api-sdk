from datetime import datetime
from typing import List, Optional

from bcs_oi_api.models.models import BCSOIAPIBaseModel

__all__ = [
    'Collector'
]


class Collector(BCSOIAPIBaseModel):
    appliance_id: str
    collector_name: str
    collector_status: str
    collector_version: str
    expected_upload_interval: int
    last_upload_timestamp: datetime

    @classmethod
    def url_path(cls):
        return 'collectors'
