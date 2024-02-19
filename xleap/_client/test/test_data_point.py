# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xleap._client.models.data_point import DataPoint


class TestDataPoint(unittest.TestCase):
    """DataPoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataPoint:
        """Test DataPoint
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `DataPoint`
        """
        model = DataPoint()
        if include_optional:
            return DataPoint(
                id = '',
                question = '',
                answer = '',
                ground_truths = [
                    null
                    ],
                result = xleap._client.models.data_point_result.DataPoint_result(
                    results = xleap._client.models.results.results(), 
                    reasons = xleap._client.models.reasons.reasons(), ),
                contexts = [
                    ''
                    ],
                tags = None
            )
        else:
            return DataPoint(
                ground_truths = [
                    null
                    ],
                result = xleap._client.models.data_point_result.DataPoint_result(
                    results = xleap._client.models.results.results(), 
                    reasons = xleap._client.models.reasons.reasons(), ),
        )
        """

    def testDataPoint(self):
        """Test DataPoint"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
