
import unittest
from HTMLTestRunner.runner import HTMLTestRunner

from add_to_cart import TestAddToCart
from add_to_favorite import TestAddToFavorite
from buttons import Buttons
from home_page_testcase import TestHomePage


test1 = unittest.TestLoader().loadTestsFromTestCase(TestAddToCart)
test2 = unittest.TestLoader().loadTestsFromTestCase(TestAddToFavorite)
test3 = unittest.TestLoader().loadTestsFromTestCase(Buttons)
test4 = unittest.TestLoader().loadTestsFromTestCase(TestHomePage)


suite = unittest.TestSuite([test1, test2, test3, test4, ])

runner = HTMLTestRunner(log=True, verbosity=5, output='report', title='Test report', report_name='report',
                        open_in_browser=True, description="HTMLTestReport", tested_by="Monica P.",
                        add_traceback=False)

runner.run(suite)
