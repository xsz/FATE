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
from federatedml.model_base import ModelBase

LOGGER = log_utils.getLogger()


class HomoBinningBase(ModelBase):
    def __init__(self, param: FeatureBinningParam=None, bin_num=10):
        super().__init__()
        self.transfer_variable = HomoFeatureBinningTransferVariable()
