# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
#
# Generated code. DO NOT EDIT!
#
# Snippet for DeleteSecret
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-secretmanager


# [START secretmanager_v1_generated_SecretManagerService_DeleteSecret_async]
from google.cloud import secretmanager_v1


async def sample_delete_secret():
    # Create a client
    client = secretmanager_v1.SecretManagerServiceAsyncClient()

    # Initialize request argument(s)
    request = secretmanager_v1.DeleteSecretRequest(
        name="name_value",
    )

    # Make the request
    await client.delete_secret(request=request)


# [END secretmanager_v1_generated_SecretManagerService_DeleteSecret_async]