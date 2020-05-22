#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    # Get figures repo root path, we are currently in devsite dir.
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Insert the project root dir to find our reusable app
    sys.path.insert(0, project_root)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devsite.settings")

    from django.core.management import execute_from_command_line

    # for path in sys.path:
    #     print(path)

    execute_from_command_line(sys.argv)
