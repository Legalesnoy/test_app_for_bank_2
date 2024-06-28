from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(l1, l1_e1):
    assert filter_by_state(l1) == l1_e1


def test_filter_by_state(l1, l1_e2):
    assert filter_by_state(l1, "CANCELED") == l1_e2


def test_sort_by_date(l2, l2_e):
    assert sort_by_date(l2) == l2_e
