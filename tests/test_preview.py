import pytest

from st_show_more import make_preview


def test_short_text_is_untouched():
    assert make_preview("hello", 10) == ("hello", False)
    assert make_preview("hello", 5) == ("hello", False)


def test_cuts_at_word_boundary():
    assert make_preview("the quick brown fox jumps", 18) == ("the quick brown…", True)


def test_cut_falling_exactly_between_words_keeps_whole_word():
    assert make_preview("the quick brown fox", 9) == ("the quick…", True)


def test_long_word_is_cut_hard():
    assert make_preview("supercalifragilistic", 8) == ("supercal…", True)


def test_dangling_punctuation_is_dropped():
    assert make_preview("adipiscing elit, sed do eiusmod", 18) == ("adipiscing elit…", True)


def test_zero_chars():
    assert make_preview("hello", 0) == ("…", True)


def test_negative_length_is_rejected():
    with pytest.raises(ValueError):
        make_preview("hello", -1)
