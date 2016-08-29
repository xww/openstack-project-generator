#!/usr/bin/env python
# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Starter script for <Project_name> Scheduler."""

import eventlet
eventlet.monkey_patch()

import sys

from oslo_config import cfg
from oslo_log import log as logging
from oslo_reports import guru_meditation_report as gmr

from <project_name> import i18n
i18n.enable_lazy()

# Need to register global_opts
from <project_name>.common import config  # noqa
from <project_name> import objects
from <project_name> import service
from <project_name> import utils
from <project_name> import version


CONF = cfg.CONF


def main():
    objects.register_all()
    CONF(sys.argv[1:], project='<project_name>',
         version=version.version_string())
    logging.setup(CONF, "<project_name>")
    utils.monkey_patch()
    gmr.TextGuruMeditation.setup_autorun(version)
    server = service.Service.create(binary='<project_name>-<manager_service_name>')
    service.serve(server)
    service.wait()
