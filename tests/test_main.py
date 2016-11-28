# -*- coding: utf-8 -*-

from SinicValidate import simple, validate


class TestSinicValidateCommands(object):

    def test_validate_phone(self):
        phone = '18888888888'
        result = validate.phone(phone)
        assert isinstance(result, dict)
        assert result['isChinaMobile']
        assert not result['isChinaUnion']
        assert not result['isChinaTelcom']
        assert not result['isOtherTelphone']
        assert result['isPhone']

        phone = '11223344556'
        result = validate.phone(phone)
        assert isinstance(result, dict)
        assert not result['isChinaMobile']
        assert not result['isChinaUnion']
        assert not result['isChinaTelcom']
        assert not result['isOtherTelphone']
        assert not result['isPhone']

    def test_validate_email(self):
        email = 'qiminis0801@gmail.com'
        result = validate.email(email)
        assert result.group() == email

        email = 'qiminis0801#gmail.com'
        result = validate.email(email)
        assert not result

    def test_simple_phone(self):
        phone = '18888888888'
        result = simple.phone(phone)
        assert result.group() == phone

        phone = '11223344556'
        result = simple.phone(phone)
        assert result.group() == phone

        phone = '112233445566'
        result = simple.phone(phone)
        assert not result
