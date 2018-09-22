# Copyright 2017 SrMouraSilva
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


import unittest
from deepbm.dbm import DBM


class DBMTest(unittest.TestCase):

    def test_assignments(self):
        visible_size = 1
        hidden1_size = 2
        hidden2_size = 3

        dbm = DBM(visible_size=visible_size, hidden1_size=hidden1_size, hidden2_size=hidden2_size)

        self.assertEqual(visible_size, dbm.visible_size)
        self.assertEqual(hidden1_size, dbm.hidden1_size)
        self.assertEqual(hidden2_size, dbm.hidden2_size)
