"""Tests for agent-eval-elo-rater."""
import unittest
from agent_eval_elo_rater.rater import EloRater


class TestEloRater(unittest.TestCase):
    def setUp(self):
        self.rater = EloRater(initial_rating=1200.0, k_factor=32.0)

    def test_win_loss_update(self):
        self.rater.record_match("a", "b", 1.0)
        self.assertGreater(self.rater.get_rating("a"), 1200.0)
        self.assertLess(self.rater.get_rating("b"), 1200.0)
        lb = self.rater.leaderboard()
        self.assertEqual(lb[0]["model"], "a")


if __name__ == "__main__":
    unittest.main()
