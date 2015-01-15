# -*- coding: utf-8 -*-
# pylint: disable=W0201, W0141
"""
Simulate build suite for nose
"""
from django.test.simple import build_suite, build_test
from django.db.models import get_app, get_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django_jenkins.tasks import BaseTask

from django_nose.runner import NoseTestSuiteRunner


class Task(BaseTask):
    pass
