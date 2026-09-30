#!/usr/bin/env python3
"""Reversibility / blast-radius scoring.

Companion to phase-1-architecture-fundamentals/week-01-what-is-architecture/reversibility-test.md

Scores a decision on four axes (1-5 each; 1, 3 and 5 are the anchors) and says
whether it is a design decision, a significant design decision, or an
architecture decision.

Usage:
    python decision_cost.py                       # interactive
    python decision_cost.py --scores 5 5 3 5      # cost, blast, teams, horizon
"""
import argparse

AXES = [
    ("Cost of change", "1 = hours/days, one team | 3 = weeks, a few teams | 5 = months, a programme or a contract"),
    ("Blast radius", "1 = one module | 3 = one system or journey | 5 = multiple systems, partners or channels"),
    ("Teams to align", "1 = none | 3 = 2-4 teams | 5 = 5+ teams or external parties"),
    ("Time horizon", "1 = until next release | 3 = 1-2 years | 5 = 5+ years or contract life"),
]

VALID = {1, 2, 3, 4, 5}


def verdict(total: int) -> str:
    if total >= 15:
        return ("ARCHITECTURE DECISION\n"
                "  -> Write an ADR (docs/adr/adr-template.md). Name the options, the\n"
                "     consequences and the dissent. Pre-work before the meeting.")
    if total >= 9:
        return ("SIGNIFICANT DESIGN DECISION\n"
                "  -> One page, two reviewers, no ceremony. Record the choice, not the debate.")
    return ("DESIGN DECISION\n"
            "  -> The owning team decides. No approval, no meeting, no architect.")


def ask():
    scores = []
    for name, hint in AXES:
        while True:
            try:
                raw = int(input(f"{name}\n  {hint}\n  Score (1-5): "))
            except ValueError:
                continue
            except EOFError:
                raise SystemExit("\nNo input. Use --scores COST BLAST TEAMS HORIZON for non-interactive use.")
            if raw in VALID:
                scores.append(raw)
                break
    return scores


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scores", nargs=4, type=int, metavar=("COST", "BLAST", "TEAMS", "HORIZON"))
    args = p.parse_args()

    scores = args.scores or ask()
    if any(s not in VALID for s in scores):
        raise SystemExit("Scores must each be between 1 and 5.")

    total = sum(scores)
    print("\n" + "-" * 58)
    for (name, _), s in zip(AXES, scores):
        print(f"{name:<18} {s}")
    print(f"{'TOTAL':<18} {total} / 20")
    print("-" * 58)
    print(verdict(total))
    print("\nRe-score when any of these change: a second team depends on it, it crosses\n"
          "an organisational or contractual boundary, it starts serving money, identity\n"
          "or regulatory data, or reversal moves from a release to a migration.")


if __name__ == "__main__":
    main()
