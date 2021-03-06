# Copyright (c) 2015 - 2016 Huawei Technologies Co., Ltd.
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

import webob

from <project_name>.api import versions
from <project_name> import test


class VersionsTest(test.TestCase):

    """Test the version information returned from the API service."""

    def test_get_version_list_public_endpoint(self):
        req = webob.Request.blank('/', base_url='http://127.0.0.1:8760/')
        req.accept = 'application/json'
        self.override_config('public_endpoint', 'https://example.com:8760')
        res = versions.Versions().index(req)
        results = res['versions']
        expected = [
            {
                'id': 'v1.0',
                'status': 'SUPPORTED',
                'updated': '2014-06-28T12:20:21Z',
                'links': [{'rel': 'self',
                           'href': 'https://example.com:8760/v1/'}],
            },
        ]
        self.assertEqual(expected, results)

    def test_get_version_list(self):
        req = webob.Request.blank('/', base_url='http://127.0.0.1:8760/')
        req.accept = 'application/json'
        res = versions.Versions().index(req)
        results = res['versions']
        expected = [
            {
                'id': 'v1.0',
                'status': 'SUPPORTED',
                'updated': '2014-06-28T12:20:21Z',
                'links': [{'rel': 'self',
                           'href': 'http://127.0.0.1:8760/v1/'}],
            },
        ]
        self.assertEqual(expected, results)

    def test_get_version_detail_v1(self):
        req = webob.Request.blank('/', base_url='http://127.0.0.1:8760/v1')
        req.accept = 'application/json'
        res = versions.<Project_name>Version().show(req)
        expected = {
            "version": {
                "status": "SUPPORTED",
                "updated": "2014-06-28T12:20:21Z",
                "media-types": [
                    {
                        "base": "application/xml",
                        "type":
                            "application/vnd.openstack.<project_name>+xml;version=1"
                    },
                    {
                        "base": "application/json",
                        "type":
                            "application/vnd.openstack.<project_name>+json;version=1"
                    }
                ],
                "id": "v1.0",
                "links": [
                    {
                        "href": "http://127.0.0.1:8760/v1/",
                        "rel": "self"
                    },
                    {
                        "href": "http://docs.openstack.org/",
                        "type": "text/html",
                        "rel": "describedby"
                    }
                ]
            }
        }
        self.assertEqual(expected, res)
