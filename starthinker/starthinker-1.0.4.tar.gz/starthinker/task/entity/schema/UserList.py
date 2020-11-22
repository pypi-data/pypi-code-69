###########################################################################
#
#  Copyright 2020 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

UserList_Schema = [
    {
        'name': 'id',
        'type': 'INTEGER',
        'mode': 'NULLABLE',
    },
    {
        'name': 'name',
        'type': 'STRING',
        'mode': 'NULLABLE',
    },
    {
        'name': 'data_partner_id',
        'type': 'INTEGER',
        'mode': 'NULLABLE',
    },
    {
        'name': 'accessing_advertisers',
        'type': 'INTEGER',
        'mode': 'REPEATED',
    },
    {
        'name':
            'partner_pricing',
        'type':
            'RECORD',
        'mode':
            'NULLABLE',
        'fields': [
            {
                'name': 'cost_type',
                'type': 'STRING',
                'mode': 'NULLABLE',
            },
            {
                'name': 'currency_code',
                'type': 'STRING',
                'mode': 'NULLABLE',
            },
            {
                'name': 'cost_micros',
                'type': 'INTEGER',
                'mode': 'NULLABLE',
            },
        ]
    },
    {
        'name':
            'advertiser_pricings',
        'type':
            'RECORD',
        'mode':
            'REPEATED',
        'fields': [
            {
                'name':
                    'pricing',
                'type':
                    'RECORD',
                'mode':
                    'NULLABLE',
                'fields': [
                    {
                        'name': 'cost_type',
                        'type': 'STRING',
                        'mode': 'NULLABLE',
                    },
                    {
                        'name': 'currency_code',
                        'type': 'STRING',
                        'mode': 'NULLABLE',
                    },
                    {
                        'name': 'cost_micros',
                        'type': 'INTEGER',
                        'mode': 'NULLABLE',
                    },
                ]
            },
            {
                'name': 'advertiser_id',
                'type': 'INTEGER',
                'mode': 'NULLABLE',
            },
        ]
    },
]
