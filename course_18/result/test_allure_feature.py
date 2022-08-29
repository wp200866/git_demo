import allure


@allure.feature("搜索模块")
class TestSearch():
    @allure.story("搜索成功")
    def test_case1(self):
        print("case1")

    @allure.story("搜索失败")
    def test_case2(self):
        print("case2")

@allure.feature("登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")
        with allure.step("步骤2：进入登录页面"):
            print("登录页面")
        with allure.step("步骤3：输入用户信息"):
            assert "1" == 2
            print("输入用户名和密码")
        with allure.step("步骤4：进入成功页面"):
            print("这是登陆：测试用例，登陆成功")

    @allure.story("登录成功")
    def test_login_success_a(self):
        print("这是登陆：测试用例，登陆成功")

    @allure.story("登录成功")
    def test_login_success_b(self):
        assert "1" == 1
        print("用户名缺失")

    @allure.story("登录失败")
    def test_login_failure(self):
        print("输入用户名")

