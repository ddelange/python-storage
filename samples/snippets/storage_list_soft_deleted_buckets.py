#!/usr/bin/env python

# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
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

# [START storage_list_soft_deleted_buckets]

from google.cloud import storage


def list_soft_deleted_buckets():
    """Lists all soft-deleted buckets."""

    storage_client = storage.Client()
    buckets = storage_client.list_buckets(soft_deleted=True)

    for bucket in buckets:
        print(bucket.name)


# [END storage_list_soft_deleted_buckets]


if __name__ == "__main__":
    list_soft_deleted_buckets()
