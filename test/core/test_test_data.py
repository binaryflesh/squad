from unittest import TestCase\

from squad.core.data import JSONTestDataParser

TEST_DATA = """
{
    "ungrouped_pass": "pass",
    "ungrouped_fail": "fail",
    "group1/pass": "pass",
    "group1/fail": "fail",
    "group2/pass": "pass",
    "group2/fail": "fail"
}
"""

json_parser = JSONTestDataParser()

class JSONTestDataParserTest(TestCase):

    def test_empty(self):
        data = json_parser("{}")
        self.assertEqual(0, len(data))

    def test_basic(self):
        data = json_parser(TEST_DATA)
        self.assertEqual(6, len(data))

    def test_test_name(self):
        test_names = [t['test_name'] for t in json_parser(TEST_DATA)]
        self.assertIn("ungrouped_pass", test_names)
        self.assertIn("pass", test_names)

    def test_group_name(self):
        group_names = [t['group_name'] for t in json_parser(TEST_DATA)]
        self.assertIn('group1', group_names)
        self.assertIn('group2', group_names)

    def test_group_and_test_name(self):
        data = json_parser(TEST_DATA)
        test = [
            t for t in data
            if t['group_name'] == 'group1' and t['test_name'] == "pass"
        ][0]
        self.assertTrue(test['pass'])

