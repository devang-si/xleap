# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xleap._client.models.list_prompts200_response import ListPrompts200Response


class TestListPrompts200Response(unittest.TestCase):
    """ListPrompts200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListPrompts200Response:
        """Test ListPrompts200Response
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ListPrompts200Response`
        """
        model = ListPrompts200Response()
        if include_optional:
            return ListPrompts200Response(
                next = '',
                previous = '',
                results = [
                    xleap._client.models.prompt.Prompt(
                        id = '', 
                        prompt = '', 
                        version = -32768, 
                        root = '', 
                        parent = '', )
                    ]
            )
        else:
            return ListPrompts200Response(
        )
        """

    def testListPrompts200Response(self):
        """Test ListPrompts200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()