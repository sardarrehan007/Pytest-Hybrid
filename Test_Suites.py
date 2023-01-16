import pytest

from Tests.Test_Cases.test_Login import Test_Login


class Test_Login1(Test_Login):

    @pytest.mark.DashboardSuite
    def test_check_dashboard(self):
        self.test_login()
