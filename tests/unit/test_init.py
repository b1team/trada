def test_sum():
    result = sum([1, 2, 3, 4])
    expected = 10
    assert result == expected


def test_failed():
    result = sum([1, 2, 3, 4])
    expected = 11
    assert result != expected
