# Copyright 2017 The Forseti Security Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Forseti installer server config object"""

from config import Config
from scripts.gcp_setup.installer.utils.constants import (
    TEMPLATE_TYPE_SERVER, DEFAULT_CLOUDSQL_INSTANCE_NAME)


class ServerConfig(Config):
    """Forseti installer server config object"""

    #Class variable initialization
    template_type = None
    cloudsql_instance = None
    cloudsql_region = None
    sendgrid_api_key = None
    notification_sender_email = None
    notification_recipient_email = None
    gsuite_superadmin_email = None

    def __init__(self, **kwargs):
        """Initialize.

        Args:
            kwargs (dict): The kwargs.
        """
        super(ServerConfig, self).__init__(**kwargs)
        self.template_type = TEMPLATE_TYPE_SERVER
        self.cloudsql_instance = '{}-{}'.format(
            DEFAULT_CLOUDSQL_INSTANCE_NAME,
            self.datetimestamp)
        self.cloudsql_region = kwargs.get('cloudsql_region') or 'us-central1'

        # forseti_conf.yaml.in properties
        self.sendgrid_api_key = kwargs.get('sendgrid_api_key')
        self.notification_sender_email = None
        self.notification_recipient_email = (
            kwargs.get('notification_recipient_email'))
        self.gsuite_superadmin_email = kwargs.get('gsuite_superadmin_email')