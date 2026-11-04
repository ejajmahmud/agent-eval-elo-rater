"""CLI for agent-eval-elo-rater."""
import sys
import argparse
from .rater import EloRater


def main():
    parser = argparse.ArgumentParser(description="Agent Eval Elo Rater")
    parser.add_argument("--demo", action="store_true", help="Run Elo demo")
    args = parser.parse_args()

    rater = EloRater()
    rater.record_match("model_flash", "model_pro", 0.0)  # Pro wins
    rater.record_match("model_custom", "model_flash", 1.0)  # Custom wins
    print(f"Leaderboard: {rater.leaderboard()}")
    sys.exit(0)


if __name__ == "__main__":
    main()
