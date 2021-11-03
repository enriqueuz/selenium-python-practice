from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtests_assertions import SearchTests

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_tests = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_tests = TestSuite([assertions_test, search_tests])

kwargs = {
    "output": "smoke-report"
}

runner = HTMLTestRunner(**kwargs)

runner.run(smoke_tests)