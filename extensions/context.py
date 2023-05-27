import datetime
from typing import Any

from copier_templates_extensions import ContextHook


class ContextUpdater(ContextHook):
    def hook(self, context: dict[str, Any]):
        return {
            "package_name": context["project_name"].replace("-", "_"),
            "current_year": datetime.datetime.now().year,
        }
