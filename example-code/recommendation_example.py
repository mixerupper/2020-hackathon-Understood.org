# -*- mode: python; coding: utf-8; -*-
from recommendation import AbstractRecommender

import pandas as pd


class ExampleRecommender(AbstractRecommender):
    def __init__(self):
        self.last_page_viewed = {}

    def observe(self, user_interaction):
        user_id = user_interaction["user_id"]
        url_path = user_interaction["url_path"]
        self.last_page_viewed[user_id] = url_path

    def recommend(self, user_id, n):
        try:
            return n * [self.last_page_viewed[user_id]]
        except KeyError:
            return n * ["/en"]


if __name__ == "__main__":
    user_interactions = pd.DataFrame(
        dict(
            row_num=range(6),
            user_id=["a", "b", "c", "a", "b", "b"],
            url_path=["/en/z", "/en/x", "/en", "/en/x", "/en/y", "/en"],
            census_key=["p", "q", "r", "p", "q", "q"],
        )
    )
    print("Test user interaction data:")
    print(user_interactions)
    print()

    n = 3
    print(f"Example site-visit and recommendation sequence:")
    user_lastpage_dict = {}
    recommender = ExampleRecommender()
    for i, (_, s) in enumerate(user_interactions.iterrows()):
        recommendations = recommender.recommend(s["user_id"], n)
        current_page = (
            user_lastpage_dict.get(s["user_id"])
            if s["user_id"] in user_lastpage_dict
            else "/en"
        )
        print(f"{i + 1}. While user {s['user_id']} views {current_page}:")
        print(f"   - We recommend {recommendations}.")
        print(f"   - User then visits {s['url_path']} at time {s['row_num']}.")
        recommender.observe(s)
        user_lastpage_dict[s["user_id"]] = s["url_path"]
