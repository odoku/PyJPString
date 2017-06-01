# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import pytest

from jpstring.converters import (
    hiragana_to_katakana,
    katakana_to_hiragana,
    numeric_to_kanji,
)


class TestHiraganaToKatakana(object):
    def test_all_chars(self):
        """
        ひらがなをカタカナにできているかどうかのテスト。
        """
        hiragana = 'ぁあぃいぅうぇえぉおかがきぎくぐけげこご' \
                   'さざしじすずせぜそぞただちぢっつづてでと' \
                   'どなにぬねのはばぱひびぴふぶぷへべぺほぼ' \
                   'ぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ'
        katakana = 'ァアィイゥウェエォオカガキギクグケゲコゴ' \
                   'サザシジスズセゼソゾタダチヂッツヅテデト' \
                   'ドナニヌネノハバパヒビピフブプヘベペホボ' \
                   'ポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ'
        assert hiragana_to_katakana(hiragana) == katakana


class TestkatakanaToHiragana(object):
    def test_all_chars(self):
        """
        カタカナをひらがなにできているかどうかのテスト。
        """
        katakana = 'ァアィイゥウェエォオカガキギクグケゲコゴ' \
                   'サザシジスズセゼソゾタダチヂッツヅテデト' \
                   'ドナニヌネノハバパヒビピフブプヘベペホボ' \
                   'ポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ'
        hiragana = 'ぁあぃいぅうぇえぉおかがきぎくぐけげこご' \
                   'さざしじすずせぜそぞただちぢっつづてでと' \
                   'どなにぬねのはばぱひびぴふぶぷへべぺほぼ' \
                   'ぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ'
        assert katakana_to_hiragana(katakana) == hiragana


class TestNumericToKanji(object):
    @pytest.mark.parametrize(
        'text, kanji_text',
        [
            ('614561456145円', '六千百四十五億六千百四十五万六千百四十五円'),
            ('111111111111円', '千百十一億千百十一万千百十一円'),
            ('100000000001円', '千億一円'),
            ('1000円', '千円'),
            ('100000円', '十万円'),
            ('1円', '一円'),
            ('0円', '〇円'),
        ]
    )
    def test_convert(self, text, kanji_text):
        """
        半角数字文字を漢字表現に変換できているかどうかのテスト。
        """
        assert numeric_to_kanji(text) == kanji_text
