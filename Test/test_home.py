from page.home import Home


class Test_Home(Home):

    def test_title(self):
        assert self.get_t()=="Amazon"
