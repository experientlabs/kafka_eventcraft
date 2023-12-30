import uuid
import random
import json

FLAG_CHANCES = {
    'empty_country_code': 0.03,
    'nonexistent_country_code': 0.02,
    'clock_really_off': 0.02,
    'repeated_events': 0.02
}

def _random_p(p: float) -> bool:
    return random.random() < p

def generate_tracking_ids_file(tracking_id_count=60):
    tracking_ids = {str(uuid.uuid4()): {} for _ in range(tracking_id_count)}

    for tracking_id, flags in tracking_ids.items():
        for flag, chance in FLAG_CHANCES.items():
            if _random_p(chance):
                flags[flag] = True

    with open("tracking_ids.json", "w") as f:
        json.dump(tracking_ids, f, indent=2)


if __name__ == '__main__':
    generate_tracking_ids_file(60)
