import allure

TEST_CASE_LINK = 'https://github.com'

@allure.link('https://ceshiren.com')
def test_with_link():
    pass

@allure.link('https://biadu.com', name='百度地址')
def test_with_name_link():
    pass

@allure.issue('140', 'pytest-flaky test retries shows like test steps')
def test_with_issue_link():
    pass

@allure.testcase(TEST_CASE_LINK, '测试管理平台')
def test_with_testcase_link():
    pass
