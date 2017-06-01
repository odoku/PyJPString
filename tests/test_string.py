# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

from jpstring import string


class TestHiragana(object):
    def test_hiragana(self):
        assert string.hiragana == (
            'ぁあぃいぅうぇえぉお'
            'かがきぎくぐけげこご'
            'さざしじすずせぜそぞ'
            'ただちぢっつづてでとど'
            'なにぬねの'
            'はばぱひびぴふぶぷへべぺほぼぽ'
            'まみむめも'
            'ゃやゅゆょよ'
            'らりるれろ'
            'ゎわゐゑをん'
            'ゔゕゖー'
        )

    def test_hiragana_dakuon(self):
        assert string.hiragana_dakuon == "がぎぐげござじずぜぞだぢづでどばびぶべぼゔ"

    def test_hiragana_handakuon(self):
        assert string.hiragana_handakuon == "ぱぴぷぺぽ"


class TestKatakana(object):
    def test_katakana(self):
        assert string.katakana == (
            'ァアィイゥウェエォオ'
            'カガキギクグケゲコゴ'
            'サザシジスズセゼソゾ'
            'タダチヂッツヅテデトド'
            'ナニヌネノ'
            'ハバパヒビピフブプヘベペホボポ'
            'マミムメモ'
            'ャヤュユョヨ'
            'ラリルレロ'
            'ヮワヰヱヲン'
            'ヴヵヶー'
        )

    def test_katakana_dakuon(self):
        assert string.katakana_dakuon == "ガギグゲゴザジズゼゾダジヅデドバビブベボヴ"

    def test_katakana_handakuon(self):
        assert string.katakana_handakuon == "パピプペポ"
