# Contributing

This repo is a record of decisions. The most valuable contribution is a better argument.

## Challenging a decision

1. Open an issue using the **Challenge a decision** template.
2. Name the decision, the fact or constraint you think was missed, and what your alternative would cost — who pays, and when.
3. If the argument holds, a **new ADR supersedes the old one**. ADRs are never edited after acceptance; the original reasoning stays visible, with a link to the record that replaced it. Your argument is credited in the new record.

## Fixing errors

Typos, broken links and arithmetic errors in templates and worked examples: open a pull request directly. Run `python tools/check_links.py` before you do.

## Ground rules

- **Anonymise everything.** No client, employer, vendor or production-system names; no real volumes, dates or security details. Describe the pattern, not the place.
- **Meridian Bank is fictional.** Keep new scenarios consistent with [`docs/meridian-bank-brief.md`](docs/meridian-bank-brief.md).
- **Numbers over adjectives.** A requirement or trade-off without a measure will be asked for one.

## Licence

By contributing you agree that content is licensed CC BY 4.0 and code in `tools/` under MIT, as described in [`LICENSE`](LICENSE).
