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

import torch


class DBM(object):
    """
    Deep Boltzmann Machine :cite:`pmlr-v5-salakhutdinov09a`

    Example of equation

    .. math::
            E(\\boldsymbol{v}, \\boldsymbol{h}) = - \\boldsymbol{h}^T\\boldsymbol{W}\\boldsymbol{v} - \\boldsymbol{v}^T\\boldsymbol{b}^v - \\boldsymbol{h}^T\\boldsymbol{b}^h

    :param visible_size:
    :param hidden1_size:
    :param hidden2_size:
    """

    def __init__(self, visible_size: int, hidden1_size: int, hidden2_size: int):
        self.visible_size = visible_size

        self.hidden1_size = hidden1_size
        self.hidden2_size = hidden2_size

        self.b_v = torch.ones(visible_size, dtype=torch.float32)
