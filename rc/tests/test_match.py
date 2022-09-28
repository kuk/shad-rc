
from rc.obj import (
    User,
    Match
)
from rc.match import gen_matches
from rc.const import (
    CITY_MODE,
    WORLDWIDE_MODE,
)


def test_even():
    users = [User(user_id=_) for _ in range(4)]
    matches = list(gen_matches(users))
    assert matches == [
        Match(user_id=0, partner_user_id=3),
        Match(user_id=1, partner_user_id=2)
    ]


def test_odd():
    users = [User(user_id=_) for _ in range(3)]
    matches = list(gen_matches(users))
    assert matches == [
        Match(user_id=0, partner_user_id=2),
        Match(user_id=1, partner_user_id=None)
    ]


def test_manual():
    users = [User(user_id=_) for _ in range(5)]
    manual_matches = [
        Match(0, 2),
        Match(1, 2),
        Match(1, 4)
    ]
    matches = list(gen_matches(users, manual_matches=manual_matches))
    assert matches == [
        Match(user_id=0, partner_user_id=2),
        Match(user_id=1, partner_user_id=4),
        Match(user_id=3, partner_user_id=None),
    ]


def test_skip():
    users = [User(user_id=_) for _ in range(5)]
    skip_matches = [
        Match(0, 1),
        Match(0, 2),
        Match(1, 2),
        Match(1, 4)
    ]
    matches = list(gen_matches(users, skip_matches=skip_matches))
    assert matches == [
        Match(user_id=0, partner_user_id=3),
        Match(user_id=1, partner_user_id=None),
        Match(user_id=4, partner_user_id=2),
    ]


def test_city_mode():
    users = [
        User(user_id=0, city='a', match_mode=CITY_MODE),
        User(user_id=1, city='a', match_mode=WORLDWIDE_MODE),
        User(user_id=2, city='a', match_mode=CITY_MODE),
    ]
    matches = list(gen_matches(users))
    assert matches == [
        Match(user_id=0, partner_user_id=2),
        Match(user_id=1, partner_user_id=None),
    ]

    users = [
        User(user_id=0, city='a', match_mode=CITY_MODE),
        User(user_id=1, city='a', match_mode=WORLDWIDE_MODE),
        User(user_id=2, city='b', match_mode=CITY_MODE),
    ]
    matches = list(gen_matches(users))
    assert matches == [
        Match(user_id=0, partner_user_id=1),
        Match(user_id=2, partner_user_id=None),
    ]

