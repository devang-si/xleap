# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xleap._client.models.project import Project


class TestProject(unittest.TestCase):
    """Project unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Project:
        """Test Project
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Project`
        """
        model = Project()
        if include_optional:
            return Project(
                id = '',
                config = xleap._client.models.project_config.Project_config(
                    metric_name_map = xleap._client.models.metric_name_map.metric_name_map(), 
                    transformer_name = '', 
                    topics = [
                        ''
                        ], 
                    nlp_scores = [
                        ''
                        ], 
                    rouge_type = '', 
                    scores = [
                        ''
                        ], ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                org = ''
            )
        else:
            return Project(
                config = xleap._client.models.project_config.Project_config(
                    metric_name_map = xleap._client.models.metric_name_map.metric_name_map(), 
                    transformer_name = '', 
                    topics = [
                        ''
                        ], 
                    nlp_scores = [
                        ''
                        ], 
                    rouge_type = '', 
                    scores = [
                        ''
                        ], ),
                name = '',
        )
        """

    def testProject(self):
        """Test Project"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()