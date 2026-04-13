"""Training content registry: imports weekly content from dedicated modules.

This file is intentionally thin. Content lives in content_weeks_X_Y.py files.
Add new weeks by creating a new content file and importing it here.
"""

from data.content_weeks_1_2 import WEEK_1, WEEK_2
from data.content_weeks_3_4 import WEEK_3, WEEK_4
from data.content_weeks_5_6 import WEEK_5, WEEK_6
from data.content_weeks_7_8 import WEEK_7, WEEK_8

WEEKS = [WEEK_1, WEEK_2, WEEK_3, WEEK_4, WEEK_5, WEEK_6, WEEK_7, WEEK_8]


def get_all_modules():
    """Return a flat list of all modules across all weeks."""
    modules = []
    for week in WEEKS:
        for mod in week["modulos"]:
            mod["semana"] = week["semana"]
            modules.append(mod)
    return modules


def get_module_by_id(module_id: str):
    """Find a module by its ID across all weeks."""
    for week in WEEKS:
        for mod in week["modulos"]:
            if mod["id"] == module_id:
                mod["semana"] = week["semana"]
                return mod
    return None


def get_week(semana: int):
    """Get a specific week\'s data by week number."""
    for week in WEEKS:
        if week["semana"] == semana:
            return week
    return None
