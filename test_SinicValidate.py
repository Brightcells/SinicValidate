# -*- coding: utf-8 -*-

import unittest

from SinicValidate import simple, validate


class SinicValidateTest(unittest.TestCase):
    # assertIsInstance、assertIsNone、assertIsNotNone
    # https://docs.python.org/2/library/unittest.html#unittest.TestCase.debug
    def testPhoneExist(self):
        phone = '18888888888'
        valphone = validate.phone(phone)
        # self.assertIsInstance(valphone, dict)
        self.assertTrue(valphone['isChinaMobile'])
        self.assertFalse(valphone['isChinaUnion'])
        self.assertFalse(valphone['isChinaTelcom'])
        self.assertFalse(valphone['isOtherTelphone'])
        self.assertTrue(valphone['isPhone'])

    def testPhoneDoesNotExist(self):
        phone = '11223344556'
        valphone = validate.phone(phone)
        # self.assertIsInstance(valphone, dict)
        self.assertFalse(valphone['isChinaMobile'])
        self.assertFalse(valphone['isChinaUnion'])
        self.assertFalse(valphone['isChinaTelcom'])
        self.assertFalse(valphone['isOtherTelphone'])
        self.assertFalse(valphone['isPhone'])

    def testEmailExist(self):
        email = 'qiminis0801@gmail.com'
        valemail = validate.email(email)
        # self.assertIsNotNone(valemail)
        self.assertEqual(valemail.group(), email)

    def testEmailDoesNotExist(self):
        email = 'qiminis0801#gmail.com'
        valemail = validate.email(email)
        # self.assertIsNone(valemail)
        self.assertEqual(valemail, None)

    def testSimplePhoneExist(self):
        phone = '18888888888'
        valphone = simple.phone(phone)
        self.assertEqual(valphone.group(), phone)

        phone = '11223344556'
        valphone = simple.phone(phone)
        self.assertEqual(valphone.group(), phone)


if __name__ == '__main__':
    unittest.main()
