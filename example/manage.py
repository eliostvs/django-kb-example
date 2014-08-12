#!/usr/bin/env python
import sys
import os

here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(here)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
