# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import pytest

from jpstring import validators


class TestValidators(object):
    @pytest.mark.parametrize('text, result', [
        ('ひらがな', True),
        ('ひら　がな', True),
        ('ひらーがな', True),
        ('カタカナ', False),
    ])
    def test_is_hiragana(self, text, result):
        assert validators.is_hiragana(text) == result

    @pytest.mark.parametrize('text, result', [
        ('カタカナ', True),
        ('カタ　カナ', True),
        ('カターカナ', True),
        ('ひらがな', False),
    ])
    def test_is_katakana(self, text, result):
        assert validators.is_katakana(text) == result

    @pytest.mark.parametrize('text, result', [
        ('1234', True),
        ('１２３４', True),
        ('一二三四', True),
        ('一〇二九〇三〇', True),
        ('一万五千四百三十二', True),
        ('3千4百', True),
        ('参萬', True),
        ('千二百十万千百二十', True),
        ('ひらがな', False),
    ])
    def test_is_numeric(self, text, result):
        assert validators.is_numeric(text) == result

    @pytest.mark.parametrize('text, split, result', [
        ('1234567', False, True),
        ('123-4567', True, True),
        ('123-4567', False, False),
        ('1234567', True, False),
        ('123456', False, False),
        ('12345678', False, False),
        ('12-4567', True, False),
        ('123-456', True, False),
        ('123-45678', True, False),
        ('1234-5678', True, False),
    ])
    def test_is_zipcode(self, text, split, result):
        assert validators.is_zipcode(text, split=split) == result

    @pytest.mark.parametrize('text, split, result', [
        # ハイフンなし
        ('0123456789', False, True),
        ('02041234567', False, True),
        ('05012345678', False, True),
        ('07012345678', False, True),
        ('08012345678', False, True),
        ('09012345678', False, True),
        ('0120123456', False, True),
        ('0570123456', False, True),
        ('0990123456', False, True),
        ('08001234567', False, True),
        ('012345678', False, False),  # 9桁
        ('012345678901', False, False),  # 12桁
        ('01012345678', False, False),
        ('03012345678', False, False),
        ('04012345678', False, False),
        ('06012345678', False, False),
        # ハイフンあり
        ('01-2345-6789', True, True),
        ('012-345-6789', True, True),
        ('0123-45-6789', True, True),
        ('01234-5-6789', True, True),
        ('050-1234-5678', True, True),
        ('070-1234-5678', True, True),
        ('080-1234-5678', True, True),
        ('090-1234-5678', True, True),
        ('0120-123-456', True, True),
        ('0570-123-456', True, True),
        ('0990-123-456', True, True),
        ('0800-123-4567', True, True),
        ('020-412-34567', True, True),
        ('0-12345-6789', True, False),
        ('01-23456-789', True, False),
        ('01-2345-678', True, False),
        ('01-2345-67890', True, False),
        ('012-345-67890', True, False),
        ('0123-45-67890', True, False),
        ('01234-5-67890', True, False),
        ('01-1-2345', True, False),
    ])
    def test_is_phone_number(self, text, split, result):
        assert validators.is_phone_number(text, split=split) == result

    @pytest.mark.parametrize('text, split, result', [
        # ハイフンなし
        ('0123456789', False, False),
        ('02041234567', False, False),
        ('05012345678', False, False),
        ('07012345678', False, True),
        ('08012345678', False, True),
        ('09012345678', False, True),
        ('0120123456', False, False),
        ('0570123456', False, False),
        ('0990123456', False, False),
        ('08001234567', False, False),
        ('012345678', False, False),  # 9桁
        ('012345678901', False, False),  # 12桁
        ('01012345678', False, False),
        ('03012345678', False, False),
        ('04012345678', False, False),
        ('06012345678', False, False),
        # ハイフンあり
        ('01-2345-6789', True, False),
        ('012-345-6789', True, False),
        ('0123-45-6789', True, False),
        ('01234-5-6789', True, False),
        ('050-1234-5678', True, False),
        ('070-1234-5678', True, True),
        ('080-1234-5678', True, True),
        ('090-1234-5678', True, True),
        ('0120-123-456', True, False),
        ('0570-123-456', True, False),
        ('0990-123-456', True, False),
        ('0800-123-4567', True, False),
        ('020-412-34567', True, False),
        ('0-12345-6789', True, False),
        ('01-23456-789', True, False),
        ('01-2345-678', True, False),
        ('01-2345-67890', True, False),
        ('012-345-67890', True, False),
        ('0123-45-67890', True, False),
        ('01234-5-67890', True, False),
        ('01-1-2345', True, False),
    ])
    def test_is_mobile_number(self, text, split, result):
        assert validators.is_mobile_number(text, split=split) == result

    @pytest.mark.parametrize('text, kwargs, result', [
        ('あいうえお', {}, 5),
        ('がぎぐげご', {'combined_chars': True}, 10),
        ('ぱぴぷぺぽ', {'combined_chars': True}, 10),
        ('アイウエオ', {}, 5),
        ('ガギグゲゴ', {'combined_chars': True}, 10),
        ('パピプペポ', {'combined_chars': True}, 10),
    ])
    def test_length(self, text, kwargs, result):
        assert validators._length(text, **kwargs) == result

    @pytest.mark.parametrize('text, max, result', [
        ('あ', 5, True),
        ('あいうえお', 5, True),
        ('あいうえお', 4, False),
    ])
    def test_max_length(self, text, max, result):
        assert validators.max_length(text, max) == result

    @pytest.mark.parametrize('text, min, result', [
        ('あ', 1, True),
        ('あい', 1, True),
        ('あいうえお', 6, False),
    ])
    def test_min_length(self, text, min, result):
        assert validators.min_length(text, min) == result

    @pytest.mark.parametrize('text, min, max, result', [
        ('あいうえお', 1, 5, True),
        ('あい', 2, 2, True),
        ('あいうえお', 6, 10, False),
        ('あいうえお', 3, 4, False),
    ])
    def test_between(self, text, min, max, result):
        assert validators.between(text, min, max) == result
