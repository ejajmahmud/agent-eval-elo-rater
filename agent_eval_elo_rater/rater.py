"""Pairwise competitive Elo rating engine for AI models."""
import math
from typing import Dict, List, Tuple, Any


class EloRater:
    def __init__(self, initial_rating: float = 1200.0, k_factor: float = 32.0):
        self.default_rating = initial_rating
        self.k_factor = k_factor
        self._ratings: Dict[str, float] = {}
        self._matches: Dict[str, int] = {}

    def get_rating(self, model_id: str) -> float:
        return self._ratings.get(model_id, self.default_rating)

    def record_match(self, model_a: str, model_b: str, score_a: float):
        """score_a: 1.0 = A wins, 0.5 = tie, 0.0 = B wins."""
        r_a = self.get_rating(model_a)
        r_b = self.get_rating(model_b)

        # Expected score formula
        e_a = 1.0 / (1.0 + math.pow(10, (r_b - r_a) / 400.0))
        e_b = 1.0 - e_a

        score_b = 1.0 - score_a

        # Update
        self._ratings[model_a] = round(r_a + self.k_factor * (score_a - e_a), 1)
        self._ratings[model_b] = round(r_b + self.k_factor * (score_b - e_b), 1)

        self._matches[model_a] = self._matches.get(model_a, 0) + 1
        self._matches[model_b] = self._matches.get(model_b, 0) + 1

    def leaderboard(self) -> List[Dict[str, Any]]:
        sorted_models = sorted(self._ratings.items(), key=lambda x: x[1], reverse=True)
        return [
            {"model": m, "rating": r, "matches": self._matches.get(m, 0)}
            for m, r in sorted_models
        ]
