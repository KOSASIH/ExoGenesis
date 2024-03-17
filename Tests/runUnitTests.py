import unittest

def runUnitTests():
    test_suite = unittest.TestSuite()

    # Add tests to the test suite
    test_suite.addTest(WidgetTestCase('test_widget_resize'))
    test_suite.addTest(WidgetTestCase('test_widget_color'))
    # Add more tests here

    # Run the test suite
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)
