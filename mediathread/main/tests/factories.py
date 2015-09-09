import factory
from django.contrib.auth.models import User
from django.test import TestCase
from quizblock.tests.test_models import FakeReq
from main.models import UserSetting, UserProfile

class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user%03d" % n)
    is_staff = False
    first_name = 'user'


class UserSettingFactory(factory.DjangoModelFactory):
    class Meta:
        model = UserSetting

    user = factory.SubFactory(UserFactory)
    name = "UserSetting"
    value = 'True'


class UserProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory)


class UserSettingTest(TestCase):
    def test_get_setting_default(self):
        self.usgetsetting = UserSetting.get_setting('self.usrset.user', 'self.usrset.name', 'default_value')
        self.assertEqual(self.usgetsetting, 'default_value')

    def test_get_setting_true(self):
        self.usrset = UserSettingFactory()
        self.usgetsetting = UserSetting.get_setting(self.usrset.user, self.usrset.name, 'default_value')
        self.assertTrue(self.usgetsetting)

    def test_get_setting_false(self):
        self.usrset = UserSettingFactory(value='False')
        self.usgetsetting = UserSetting.get_setting(self.usrset.user, self.usrset.name, 'default_value')
        self.assertFalse(self.usgetsetting)

    def test_get_setting_value(self):
        self.usrset = UserSettingFactory(value='some_other_value')
        self.usgetsetting = UserSetting.get_setting(self.usrset.user, self.usrset.name, 'default_value')
        self.assertEqual(self.usgetsetting, 'some_other_value')

    def test_set_setting_value_exception(self):
        self.usr = UserFactory()
        self.usgetsetting = UserSetting.set_setting(self.usr, 'setting_name', value='True')
        self.assertEqual(self.usgetsetting, 'some_other_value')

    def test_set_setting_value(self):
        self.usrset = UserSettingFactory()
        self.usgetsetting = UserSetting.set_setting(self.usrset.user, self.usrset.name, value='False')
        self.assertEqual(self.usrset.value, 'False')
