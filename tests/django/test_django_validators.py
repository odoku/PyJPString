# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import pytest

from django.core.exceptions import ValidationError
from jpstring.django import validators


class TestHiraganaValidator(object):
    @pytest.mark.parametrize('text', [
        'ひらがな',
        'ひら　がな',
        'ひらーがな',
    ])
    def test_valid(self, text):
        v = validators.HiraganaValidator()
        v(text)

    @pytest.mark.parametrize('text', [
        'カタカナ',
    ])
    def test_invalid(self, text):
        v = validators.HiraganaValidator()
        with pytest.raises(ValidationError):
            v(text)


class TestKatakanaValidator(object):
    @pytest.mark.parametrize('text', [
        'カタカナ',
        'カタ　カナ',
        'カターカナ',
    ])
    def test_valid(self, text):
        v = validators.KatakanaValidator()
        v(text)

    @pytest.mark.parametrize('text', [
        'ひらがな',
    ])
    def test_invalid(self, text):
        v = validators.KatakanaValidator()
        with pytest.raises(ValidationError):
            v(text)


class TestNumericValidator(object):
    @pytest.mark.parametrize('text', [
        '1234',
        '１２３４',
        '一二三四',
        '一〇二九〇三〇',
        '一万五千四百三十二',
        '3千4百',
        '参萬',
        '千二百十万千百二十',
    ])
    def test_valid(self, text):
        v = validators.NumericValidator()
        v(text)

    @pytest.mark.parametrize('text', [
        'ひらがな',
    ])
    def test_invalid(self, text):
        v = validators.NumericValidator()
        with pytest.raises(ValidationError):
            v(text)


class TestZipcodeValidator(object):
    @pytest.mark.parametrize('text, split', [
        # ハイフンなし
        ('1234567', False),
        # ハイフンあり
        ('123-4567', True),
    ])
    def test_valid(self, text, split):
        v = validators.ZipcodeValidator(split=split)
        v(text)

    @pytest.mark.parametrize('text, split', [
        # ハイフンなし
        ('123-4567', False),
        ('1234567', True),
        ('123456', False),
        ('12345678', False),
        # ハイフンあり
        ('12-4567', True),
        ('123-456', True),
        ('123-45678', True),
        ('1234-5678', True),
    ])
    def test_invalid(self, text, split):
        v = validators.ZipcodeValidator(split=split)
        with pytest.raises(ValidationError):
            v(text)


class TestPhoneNumberValidator(object):
    @pytest.mark.parametrize('text, split', [
        # ハイフンなし
        ('0123456789', False),
        ('02041234567', False),
        ('05012345678', False),
        ('07012345678', False),
        ('08012345678', False),
        ('09012345678', False),
        ('0120123456', False),
        ('0570123456', False),
        ('0990123456', False),
        ('08001234567', False),
        # ハイフンあり
        ('01-2345-6789', True),
        ('012-345-6789', True),
        ('0123-45-6789', True),
        ('01234-5-6789', True),
        ('050-1234-5678', True),
        ('070-1234-5678', True),
        ('080-1234-5678', True),
        ('090-1234-5678', True),
        ('0120-123-456', True),
        ('0570-123-456', True),
        ('0990-123-456', True),
        ('0800-123-4567', True),
        ('020-412-34567', True),
    ])
    def test_valid(self, text, split):
        v = validators.PhoneNumberValidator(split=split)
        v(text)

    @pytest.mark.parametrize('text, split', [
        # ハイフンなし
        ('012345678', False),  # 9桁
        ('012345678901', False),  # 12桁
        ('01012345678', False),
        ('03012345678', False),
        ('04012345678', False),
        ('06012345678', False),
        # ハイフンあり
        ('0-12345-6789', True),
        ('01-23456-789', True),
        ('01-2345-678', True),
        ('01-2345-67890', True),
        ('012-345-67890', True),
        ('0123-45-67890', True),
        ('01234-5-67890', True),
        ('01-1-2345', True),
    ])
    def test_invalid(self, text, split):
        v = validators.PhoneNumberValidator(split=split)
        with pytest.raises(ValidationError):
            v(text)


class TestMobileNumberValidator(object):
    @pytest.mark.parametrize('text, split', [
        # ハイフンなし
        ('07012345678', False),
        ('08012345678', False),
        ('09012345678', False),
        # ハイフンあり
        ('070-1234-5678', True),
        ('080-1234-5678', True),
        ('090-1234-5678', True),
    ])
    def test_valid(self, text, split):
        v = validators.MobileNumberValidator(split=split)
        v(text)

    @pytest.mark.parametrize('text, split', [
        # ハイフンなし
        ('0123456789', False),
        ('02041234567', False),
        ('05012345678', False),
        ('0120123456', False),
        ('0570123456', False),
        ('0990123456', False),
        ('08001234567', False),
        ('012345678', False),  # 9桁
        ('012345678901', False),  # 12桁
        ('01012345678', False),
        ('03012345678', False),
        ('04012345678', False),
        ('06012345678', False),
        # ハイフンあり
        ('01-2345-6789', True),
        ('012-345-6789', True),
        ('0123-45-6789', True),
        ('01234-5-6789', True),
        ('050-1234-5678', True),
        ('0120-123-456', True),
        ('0570-123-456', True),
        ('0990-123-456', True),
        ('0800-123-4567', True),
        ('020-412-34567', True),
        ('0-12345-6789', True),
        ('01-23456-789', True),
        ('01-2345-678', True),
        ('01-2345-67890', True),
        ('012-345-67890', True),
        ('0123-45-67890', True),
        ('01234-5-67890', True),
        ('01-1-2345', True),
    ])
    def test_invalid(self, text, split):
        v = validators.MobileNumberValidator(split=split)
        with pytest.raises(ValidationError):
            v(text)


class TestMaxLengthValidator(object):
    @pytest.mark.parametrize('text, max', [
        ('あ', 5),
        ('あいうえお', 5),
    ])
    def test_valid(self, text, max):
        v = validators.MaxLengthValidator(max=max)
        v(text)

    @pytest.mark.parametrize('text, max', [
        ('あいうえお', 4),
    ])
    def test_invalid(self, text, max):
        v = validators.MaxLengthValidator(max=max)
        with pytest.raises(ValidationError):
            v(text)


class TestMinLengthValidator(object):
    @pytest.mark.parametrize('text, min', [
        ('あ', 1),
        ('あい', 1),
    ])
    def test_valid(self, text, min):
        v = validators.MinLengthValidator(min=min)
        v(text)

    @pytest.mark.parametrize('text, min', [
        ('あいうえお', 6),
    ])
    def test_invalid(self, text, min):
        v = validators.MinLengthValidator(min=min)
        with pytest.raises(ValidationError):
            v(text)


class TestBetweenValidator(object):
    @pytest.mark.parametrize('text, min, max', [
        ('あいうえお', 1, 5),
        ('あい', 2, 2),
    ])
    def test_valid(self, text, min, max):
        v = validators.BetweenValidator(min=min, max=max)
        v(text)

    @pytest.mark.parametrize('text, min, max', [
        ('あいうえお', 6, 10),
        ('あいうえお', 3, 4),
    ])
    def test_invalid(self, text, min, max):
        v = validators.BetweenValidator(min=min, max=max)
        with pytest.raises(ValidationError):
            v(text)
