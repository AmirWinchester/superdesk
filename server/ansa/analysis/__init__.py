# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2016 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license

import superdesk

from .analysis import AnalysisResource, AnalysisService, SEMANTICS_SCHEMA


def init_app(app):
    endpoint_name = 'analysis'
    service = AnalysisService(endpoint_name, backend=superdesk.get_backend())
    AnalysisResource(endpoint_name, app=app, service=service)
    superdesk.register_item_schema_field('semantics', SEMANTICS_SCHEMA, app)
