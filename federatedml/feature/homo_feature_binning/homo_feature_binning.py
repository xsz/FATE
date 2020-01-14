#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from arch.api.utils import log_utils
from federatedml.transfer_variable.transfer_class.homo_feature_binning_transfer_variable import \
    HomoFeatureBinningTransferVariable
from federatedml.param.feature_binning_param import FeatureBinningParam
from federatedml.feature.homo_feature_binning.base_homo_binning import HomoBinningBase

LOGGER = log_utils.getLogger()


class HomoBinningArbiter(HomoBinningBase):
    """
    Do binning method through guest and host

    """
    def __init__(self, param):
        super().__init__(param)

    def aggregate_split_points(self, suffix=tuple()):
        guest_split_points = self.transfer_variable.guest_split_points.get(idx=0, suffix=suffix)
        host_split_points_list = self.transfer_variable.host_split_points.get(idx=-1, suffix=suffix)
        client_split_points = [guest_split_points] + host_split_points_list
        merged_split_points = self.merge_split_points(client_split_points)
        return merged_split_points

    def merge_split_points(self, client_split_points):

        return client_split_points


class HomoBinningClient(HomoBinningBase):
    def __init__(self, role, param):
        super().__init__(param)
        self.role = role
        self.transfer_variable = HomoFeatureBinningTransferVariable()

    def