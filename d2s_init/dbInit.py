import pymongo

false = False; true = True
dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
d2s_db = dbclient["d2s"]
d2s_in_progress_game_col = d2s_db["d2s_in_progress_game"]

docDemo = [
    {
        "spectators": 2,
        "dire_series_wins": 0,
        "league_id": 4122,
        "radiant_series_wins": 0,
        "league_node_id": 0,
        "stream_delay_s": 120,
        "series_type": 0,
        "players": [
            {
                "name": "FACEIT.com | Lasherhoneysuckle B",
                "hero_id": 0,
                "team": 4,
                "account_id": 292936649
            },
            {
                "name": "all aboard the deboost train",
                "hero_id": 69,
                "team": 0,
                "account_id": 86820903
            },
            {
                "name": "Dende",
                "hero_id": 64,
                "team": 1,
                "account_id": 196363062
            },
            {
                "name": "acc bayer",
                "hero_id": 93,
                "team": 0,
                "account_id": 39861186
            },
            {
                "name": "M0jo-J0jo",
                "hero_id": 31,
                "team": 0,
                "account_id": 25486188
            },
            {
                "name": "oops",
                "hero_id": 22,
                "team": 1,
                "account_id": 93971681
            },
            {
                "name": "Ossi (Dog)",
                "hero_id": 15,
                "team": 1,
                "account_id": 96622888
            },
            {
                "name": "31",
                "hero_id": 23,
                "team": 1,
                "account_id": 193303894
            },
            {
                "name": "Testeri ^^ :> :<\u00af\\\\ _(\u30c4)_ /\u00af",
                "hero_id": 90,
                "team": 0,
                "account_id": 66691128
            },
            {
                "name": "JuliKnowsBest",
                "hero_id": 120,
                "team": 1,
                "account_id": 72856820
            },
            {
                "name": "Obvi\u00f6slicher (Di)vinegenie\u00dfer",
                "hero_id": 18,
                "team": 0,
                "account_id": 92940915
            }
        ],
        "lobby_id": 26449967271594908,
        "match_id": 5158532034,
        "scoreboard": {
            "dire": {
                "score": 10,
                "abilities": [
                    {
                        "ability_id": 5110,
                        "ability_level": 1
                    },
                    {
                        "ability_id": 5111,
                        "ability_level": 4
                    },
                    {
                        "ability_id": 5112,
                        "ability_level": 1
                    },
                    {
                        "ability_id": 5113,
                        "ability_level": 1
                    },
                    {
                        "ability_id": 5669,
                        "ability_level": 1
                    }
                ],
                "picks": [
                    {
                        "hero_id": 64
                    },
                    {
                        "hero_id": 15
                    },
                    {
                        "hero_id": 22
                    },
                    {
                        "hero_id": 23
                    },
                    {
                        "hero_id": 120
                    }
                ],
                "barracks_state": 63,
                "tower_state": 2039,
                "players": [
                    {
                        "death": 1,
                        "item2": 11,
                        "ultimate_cooldown": 0,
                        "denies": 13,
                        "respawn_timer": 0,
                        "gold": 767,
                        "player_slot": 128,
                        "item0": 239,
                        "kills": 1,
                        "assists": 4,
                        "position_x": 6703.12255859375,
                        "item4": 166,
                        "item3": 38,
                        "position_y": 6294.51708984375,
                        "ultimate_state": 3,
                        "last_hits": 76,
                        "item1": 180,
                        "hero_id": 120,
                        "level": 10,
                        "net_worth": 5567,
                        "gold_per_min": 374,
                        "item5": 17,
                        "xp_per_min": 344,
                        "account_id": 72856820
                    },
                    {
                        "death": 2,
                        "item2": 172,
                        "ultimate_cooldown": 48,
                        "denies": 13,
                        "respawn_timer": 0,
                        "gold": 837,
                        "player_slot": 129,
                        "item0": 354,
                        "kills": 4,
                        "assists": 1,
                        "position_x": 3859.16748046875,
                        "item4": 36,
                        "item3": 50,
                        "position_y": 753.6343994140625,
                        "ultimate_state": 1,
                        "last_hits": 79,
                        "item1": 75,
                        "hero_id": 15,
                        "level": 11,
                        "net_worth": 6102,
                        "gold_per_min": 374,
                        "item5": 306,
                        "xp_per_min": 421,
                        "account_id": 96622888
                    },
                    {
                        "death": 2,
                        "item2": 36,
                        "ultimate_cooldown": 23,
                        "denies": 10,
                        "respawn_timer": 0,
                        "gold": 813,
                        "player_slot": 130,
                        "item0": 375,
                        "kills": 2,
                        "assists": 1,
                        "position_x": 6199.06396484375,
                        "item4": 13,
                        "item3": 11,
                        "position_y": -2402.9150390625,
                        "ultimate_state": 1,
                        "last_hits": 90,
                        "item1": 267,
                        "hero_id": 23,
                        "level": 10,
                        "net_worth": 6053,
                        "gold_per_min": 379,
                        "item5": 50,
                        "xp_per_min": 373,
                        "account_id": 193303894
                    },
                    {
                        "death": 4,
                        "item2": 36,
                        "ultimate_cooldown": 11,
                        "denies": 1,
                        "respawn_timer": 0,
                        "gold": 456,
                        "player_slot": 131,
                        "item0": 214,
                        "kills": 0,
                        "assists": 6,
                        "position_x": 5407.2841796875,
                        "item4": 0,
                        "item3": 218,
                        "position_y": 4193.1025390625,
                        "ultimate_state": 1,
                        "last_hits": 9,
                        "item1": 0,
                        "hero_id": 64,
                        "level": 6,
                        "net_worth": 2406,
                        "gold_per_min": 190,
                        "item5": 265,
                        "xp_per_min": 150,
                        "account_id": 196363062
                    },
                    {
                        "death": 4,
                        "item2": 0,
                        "ultimate_cooldown": 37,
                        "denies": 2,
                        "respawn_timer": 0,
                        "gold": 886,
                        "player_slot": 132,
                        "item0": 36,
                        "kills": 3,
                        "assists": 0,
                        "position_x": 6436.7216796875,
                        "item4": 244,
                        "item3": 180,
                        "position_y": 3578.01708984375,
                        "ultimate_state": 1,
                        "last_hits": 5,
                        "item1": 0,
                        "hero_id": 22,
                        "level": 7,
                        "net_worth": 3036,
                        "gold_per_min": 196,
                        "item5": 0,
                        "xp_per_min": 223,
                        "account_id": 93971681
                    }
                ],
                "bans": [
                    {
                        "hero_id": 70
                    },
                    {
                        "hero_id": 126
                    },
                    {
                        "hero_id": 6
                    }
                ]
            },
            "radiant": {
                "score": 13,
                "abilities": [
                    {
                        "ability_id": 5494,
                        "ability_level": 4
                    },
                    {
                        "ability_id": 5495,
                        "ability_level": 4
                    },
                    {
                        "ability_id": 5496,
                        "ability_level": 2
                    },
                    {
                        "ability_id": 5497,
                        "ability_level": 2
                    },
                    {
                        "ability_id": 6137,
                        "ability_level": 1
                    },
                    {
                        "ability_id": 5669,
                        "ability_level": 1
                    }
                ],
                "picks": [
                    {
                        "hero_id": 31
                    },
                    {
                        "hero_id": 69
                    },
                    {
                        "hero_id": 90
                    },
                    {
                        "hero_id": 18
                    },
                    {
                        "hero_id": 93
                    }
                ],
                "barracks_state": 63,
                "tower_state": 2046,
                "players": [
                    {
                        "death": 2,
                        "item2": 36,
                        "ultimate_cooldown": 71,
                        "denies": 10,
                        "respawn_timer": 0,
                        "gold": 933,
                        "player_slot": 0,
                        "item0": 355,
                        "kills": 3,
                        "assists": 2,
                        "position_x": 3583.3603515625,
                        "item4": 63,
                        "item3": 162,
                        "position_y": -3766.593017578125,
                        "ultimate_state": 1,
                        "last_hits": 115,
                        "item1": 71,
                        "hero_id": 18,
                        "level": 12,
                        "net_worth": 6908,
                        "gold_per_min": 425,
                        "item5": 172,
                        "xp_per_min": 492,
                        "account_id": 92940915
                    },
                    {
                        "death": 4,
                        "item2": 214,
                        "ultimate_cooldown": 0,
                        "denies": 0,
                        "respawn_timer": 0,
                        "gold": 448,
                        "player_slot": 1,
                        "item0": 36,
                        "kills": 1,
                        "assists": 2,
                        "position_x": -6074.66162109375,
                        "item4": 0,
                        "item3": 43,
                        "position_y": 1536.5350341796875,
                        "ultimate_state": 3,
                        "last_hits": 18,
                        "item1": 265,
                        "hero_id": 90,
                        "level": 7,
                        "net_worth": 2748,
                        "gold_per_min": 163,
                        "item5": 94,
                        "xp_per_min": 188,
                        "account_id": 66691128
                    },
                    {
                        "death": 4,
                        "item2": 218,
                        "ultimate_cooldown": 26,
                        "denies": 0,
                        "respawn_timer": 0,
                        "gold": 597,
                        "player_slot": 2,
                        "item0": 0,
                        "kills": 2,
                        "assists": 3,
                        "position_x": -4950.015625,
                        "item4": 0,
                        "item3": 0,
                        "position_y": -1186.525634765625,
                        "ultimate_state": 1,
                        "last_hits": 4,
                        "item1": 180,
                        "hero_id": 31,
                        "level": 7,
                        "net_worth": 2347,
                        "gold_per_min": 165,
                        "item5": 0,
                        "xp_per_min": 187,
                        "account_id": 25486188
                    },
                    {
                        "death": 0,
                        "item2": 11,
                        "ultimate_cooldown": 0,
                        "denies": 11,
                        "respawn_timer": 0,
                        "gold": 503,
                        "player_slot": 3,
                        "item0": 1,
                        "kills": 4,
                        "assists": 2,
                        "position_x": 5055.1923828125,
                        "item4": 12,
                        "item3": 50,
                        "position_y": -3697.61767578125,
                        "ultimate_state": 3,
                        "last_hits": 77,
                        "item1": 36,
                        "hero_id": 69,
                        "level": 11,
                        "net_worth": 7933,
                        "gold_per_min": 472,
                        "item5": 185,
                        "xp_per_min": 387,
                        "account_id": 86820903
                    },
                    {
                        "death": 0,
                        "item2": 185,
                        "ultimate_cooldown": 16,
                        "denies": 7,
                        "respawn_timer": 0,
                        "gold": 680,
                        "player_slot": 4,
                        "item0": 11,
                        "kills": 2,
                        "assists": 2,
                        "position_x": 3224.734130859375,
                        "item4": 181,
                        "item3": 50,
                        "position_y": -4498.3876953125,
                        "ultimate_state": 1,
                        "last_hits": 99,
                        "item1": 75,
                        "hero_id": 93,
                        "level": 13,
                        "net_worth": 6070,
                        "gold_per_min": 368,
                        "item5": 304,
                        "xp_per_min": 536,
                        "account_id": 39861186
                    }
                ],
                "bans": [
                    {
                        "hero_id": 40
                    },
                    {
                        "hero_id": 97
                    },
                    {
                        "hero_id": 83
                    }
                ]
            },
            "duration": 962.098388671875,
            "roshan_respawn_timer": 0
        }
    }
]

x = d2s_in_progress_game_col.insert_many(docDemo)
print(x.inserted_ids)


