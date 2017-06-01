# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import pytest

from jpstring.normalizers import (
    normalize_numeric,
    normalize_text,
)


class TestNormalizeText(object):
    @pytest.mark.parametrize(
        'text, normalized_text',
        [
            ('１２３４', '1234'),
            ('ＡＢＣＤａｂｃｄ', 'ABCDabcd'),
            ('ﾎｹﾞﾎｹﾞ', 'ホゲホゲ'),
            ('ホ゜ケ゛ホ゜ケ゛', 'ポゲポゲ'),
            ('ほげほげ', 'ほげほげ'),
            ('‐', '-'),
            ('‑', '-'),
            ('‒', '-'),
            ('–', '-'),
            ('—', '-'),
            ('―', '-'),
            ('⁃', '-'),
            ('−', '-'),
            ('1－2－3', '1-2-3'),
            ('１ー２ー３', '1-2-3'),
            ('ベースボール', 'ベースボール'),
        ]
    )
    def test_normalize(self, text, normalized_text):
        """
        文字列を正しく正規化できているかどうかのテスト。
        """
        assert normalize_text(text) == normalized_text


class TestNormalizeNumeric(object):
    @pytest.mark.parametrize(
        'text, normalized_text',
        [
            ('10000', '10000'),
            ('１２３４', '1234'),
            ('一二三四', '1234'),
            ('一〇二九〇三〇', '1029030'),
            ('一万五千四百三十二円', '15432円'),
            ('3千4百円', '3400円'),
            ('1万5千4百円', '15400円'),
            ('一三万円', '130000円'),
            ('参萬円', '30000円'),
            ('十円', '10円'),
            ('百万円', '1000000円'),
            ('千二百十万千百二十円', '12101120円'),
            ('一三万5千200円三五銭', '135200円35銭'),
            ('一三万5千200円三十五銭', '135200円35銭'),
            ('10.5万円', '105000円'),
            ('１０．５万円', '105000円'),
            ('10,000円', '10000円'),
            ('１０，０００円', '10000円'),
            ('二十．五円', '20.5円'),
        ]
    )
    def test_normalize(self, text, normalized_text):
        """
        文字列中の数字文字を正しく正規化できているかどうかのテスト。
        """
        assert normalize_numeric(text) == normalized_text
