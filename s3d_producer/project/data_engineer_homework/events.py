import random
from datetime import datetime, timedelta
from typing import Dict, Optional
import numpy as np
import json

INVALID_COUNTRIES = ["GB", "EU"]

REPEATING_EVENTS_CHANCE = 0.35
REPEATING_EVENTS_STOP_CHANCE = 0.15
COUNTRY_CODE_CHANGE_CHANCE = 0.01


class User:

    tracking_id: str
    country_code: str
    app_store_country: str
    flags: Dict[str, bool]
    clock_offset: timedelta
    repeated_event: Optional[dict]

    def __init__(self, tracking_id, country_code, flags):
        self.tracking_id = tracking_id
        self.country_code = country_code[0]
        self.app_store_country = country_code[1]
        self.flags = flags
        self.repeated_event = None

        if "clock_really_off" in flags.keys():
            self.clock_offset = timedelta(
                days=np.random.normal(loc=0, scale=(365 * 10)),
                seconds=np.random.normal(loc=0, scale=(12 * 60 * 60)),
            )
        else:
            self.clock_offset = timedelta(seconds=np.random.normal())

        if "nonexistent_country_code" in flags.keys():
            self.country_code = random.choice(INVALID_COUNTRIES)

        if "empty_country_code" in flags.keys():
            self.country_code = ""


class RandomEventGenerator:

    EVENT_NAMES = [
        "app_launched",
        "app_activated",
        "app_deactivated",
        "arc_added",
        "circle_added",
        "color_set",
        "drawing_created",
        "drawing_deleted",
        "drawing_opened",
        "drawing_updated",
        "nps_score_submitted",
        "onboarding_tutorial_finished",
        "screenshot_created",
        "resource_imported",
        "spline_added",
        "workspace_created",
        "workspace_export_saving_initiated",
        "workspace_opened",
        "app_crashed",
        "line_added",
        "push_notification_set",
        "object_deleted",
        "objects_aligned",
        "objects_copied",
        "objects_mirrored",
        "objects_rotated",
        "objects_scaled",
        "objects_translated",
        "onboarding_tutorial_step_completed",
        "parallel_constraint_set",
        "perpendicular_constraint_set",
        "input_device_selected",
        "update_accepted",
        "update_canceled",
        "user_logged_in",
        "user_signed_up",
    ]
    PLATFORMS = ["macOS", "iOS"]

    def __init__(self, country_codes: list, tracking_ids: dict):
        self.country_codes = country_codes
        self.tracking_ids = [
            User(tracking_id, random.choice(self.country_codes), flags)
            for tracking_id, flags in tracking_ids.items()
        ]
        self.repeated_event = None

    def _random_p(self, p: float) -> bool:
        return random.random() < p

    def get_event(self):
        if self.repeated_event:
            event = self.repeated_event
            if self._random_p(REPEATING_EVENTS_STOP_CHANCE):
                self.repeated_event = None
            return event

        user = random.choice(list(self.tracking_ids))
        platform = "macOS"
        if self._random_p(0.05):
            platform = "iOS"

        current_time = datetime.now()
        network_latency = timedelta(
            seconds=max(0.1, np.random.normal(loc=10.0, scale=3.0))
        )

        event_time = current_time - network_latency - user.clock_offset
        client_upload_time = current_time - user.clock_offset
        server_upload_time = current_time

        if (
            self._random_p(COUNTRY_CODE_CHANGE_CHANCE)
            and "empty_country_code" not in user.flags
        ):
            new_country_code = random.choice(self.country_codes)
            user.country_code = new_country_code[0]
            user.app_store_country = new_country_code[1]

        event = dict(
            user_id=user.tracking_id,
            event_time=event_time.isoformat(),
            server_upload_time=server_upload_time.isoformat(),
            client_upload_time=client_upload_time.isoformat(),
            event_name=random.choice(self.EVENT_NAMES),
            platform=platform,
            country_code=user.country_code,
            app_store_country=user.app_store_country,
        )

        if "repeated_events" in user.flags and self._random_p(REPEATING_EVENTS_CHANCE):
            self.repeated_event = event

        return event
