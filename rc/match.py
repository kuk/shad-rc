
import random
from collections import defaultdict

from .obj import Match
from .const import CITY_MODE


def gen_matches(users, skip_matches=(), manual_matches=(), seed=0):
    random.seed(seed)

    user_ids = {_.user_id for _ in users}

    skip_matches_index = defaultdict(set)
    for match in skip_matches:
        skip_matches_index[match.user_id].add(match.partner_user_id)
        skip_matches_index[match.partner_user_id].add(match.user_id)

    manual_matches_index = defaultdict(set)
    for match in manual_matches:
        if (
                match.user_id in user_ids and match.partner_user_id in user_ids
                and match.partner_user_id not in skip_matches_index[match.user_id]
        ):
            manual_matches_index[match.user_id].add(match.partner_user_id)
            manual_matches_index[match.partner_user_id].add(match.user_id)

    def key(user):
        has_manual_match = user.user_id in manual_matches_index
        match_city = user.match_mode == CITY_MODE

        return (
            has_manual_match,
            match_city,

            # shuffle inside groups
            random.random()
        )

    users = sorted(users, key=key, reverse=True)

    matched_user_ids = set()
    for user in users:
        if user.user_id in matched_user_ids:
            continue

        # <100 users per week, ok N(O^2) algo
        partner_users = [
            _ for _ in users
            if _.user_id != user.user_id
            if _.user_id not in matched_user_ids
            if _.user_id not in skip_matches_index[user.user_id]
        ]

        partner_user_id = None
        if partner_users:

            def key(partner_user, user=user):
                is_manual_match = partner_user.user_id in manual_matches_index[user.user_id]

                if user.match_mode == CITY_MODE:
                    same_city = user.city == partner_user.city
                    both_match_city = partner_user.match_mode == CITY_MODE

                    return (
                        is_manual_match,
                        same_city,
                        both_match_city
                    )

                else:
                    return (
                        is_manual_match,
                        random.random()
                    )

            partner_users = sorted(partner_users, key=key, reverse=True)
            partner_user_id = partner_users[0].user_id

        matched_user_ids.add(user.user_id)
        matched_user_ids.add(partner_user_id)
        yield Match(user.user_id, partner_user_id)
