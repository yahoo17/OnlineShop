import unittest
import sys
sys.path.append("..")
from flaskServer.userinfo import *

#
# 以test开头的方法会被测试
class UserInfoTestCase(unittest.TestCase):
    def test_password_setter(self):
        u=UserInfo(password='cat')
        self.assertTrue(u.password_hash is not None)
        # 断言函数u.password_hash 不为空


    def test_no_password_getter(self):
        u=UserInfo(password='cat')
        with self.assertRaises(AttributeError):
            u.password
        
    def test_password_verification(self):
        u=UserInfo(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.veritfy_password('dog'))

    def test_password_salts_are_random(self):
        u=UserInfo(password='cat')
        u2=UserInfo(password='cat')
        self.assertNotEqual(u.password_hash,u2.password_hash)

if __name__=='__main__':
    unittest.main()