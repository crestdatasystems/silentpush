# File: test_widget_templates.py
#
# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.

import re
from pathlib import Path


def test_context_menu_values_use_javascript_escaping():
    """Require JavaScript-context escaping for every custom-menu value."""
    unsafe_values = []

    for template in (Path(__file__).parent.parent / "views").glob("*.html"):
        content = template.read_text(encoding="utf-8")
        for value in re.findall(r"'value': '\{\{([^}]*)\}\}'", content):
            if "|escapejs" not in value:
                unsafe_values.append(f"{template.name}: {value.strip()}")

    assert not unsafe_values, f"Unescaped JavaScript context-menu values: {unsafe_values}"
