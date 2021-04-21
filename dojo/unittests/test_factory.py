from django.test import TestCase
from dojo.tools.factory import import_parser_factory, get_disabled_scanners, get_choices
from dojo.models import Test


class TestFactory(TestCase):

    fixtures = ["dojo_tool_type.json"]

    def test_acunetix_one_finding(self):
        testfile = open('dojo/unittests/scans/acunetix/one_finding.xml')
        parser = import_parser_factory(testfile, Test(), False, False, 'Acunetix Scan')
        findings = parser.get_findings(testfile, Test())
        testfile.close()
        self.assertEqual(1, len(findings))

    def test_anchore_one_finding(self):
        testfile = open("dojo/unittests/scans/anchore/one_vuln.json")
        parser = import_parser_factory(testfile, Test(), False, False, 'Anchore Engine Scan')
        findings = parser.get_findings(testfile, Test())
        testfile.close()
        self.assertEqual(1, len(findings))

    def test_nessus(self):
        testfile = open("dojo/unittests/scans/nessus/nessus_v_unknown.xml")
        parser = import_parser_factory(testfile, Test(), False, False, 'Nessus Scan')
        findings = parser.get_findings(testfile, Test())
        testfile.close()
        self.assertEqual(32, len(findings))

    def test_disabled_scanners(self):
        self.assertEqual(1, len(get_disabled_scanners()))

    def test_not_acunetix_scan(self):
        for choice in get_choices():
            self.assertFalse("Acunetix Scan" in  choice[0])
        assert True
