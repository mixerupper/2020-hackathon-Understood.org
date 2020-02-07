# -*- mode: python; coding: utf-8; -*-
from abc import ABC, abstractmethod


class AbstractRecommender(ABC):
    @abstractmethod
    def observe(self, user_interaction):
        """Observe user interaction event as a Pandas Series."""
        pass

    @abstractmethod
    def recommend(self, user_id, n):
        """Return a list of n recommendations for a given user."""
        pass
