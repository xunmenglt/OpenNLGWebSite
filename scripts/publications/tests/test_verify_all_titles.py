import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from publication_lib import load_venues
from verify_all_titles import choose_conference_evidence, is_verified_in_range


class VerifyAllTitlesTests(unittest.TestCase):
    def test_accepts_only_external_allowlisted_venue_evidence(self):
        venues = load_venues(ROOT / "venues.json")
        evidence, venue = choose_conference_evidence(
            [
                {"provider": "DBLP", "matched": True, "source": "arXiv preprint", "authors": "A"},
                {"provider": "Crossref", "matched": True, "source": "Proceedings of ACL 2026", "authors": "A"},
            ],
            venues,
        )
        self.assertEqual("ACL", venue)
        self.assertEqual("Crossref", evidence["provider"])

    def test_rejects_unmatched_venue_evidence(self):
        venues = load_venues(ROOT / "venues.json")
        evidence, venue = choose_conference_evidence(
            [{"provider": "DBLP", "matched": True, "source": "arXiv preprint", "authors": "A"}], venues
        )
        self.assertIsNone(evidence)
        self.assertIsNone(venue)

    def test_strict_output_requires_verified_conference_and_year(self):
        self.assertTrue(is_verified_in_range({"status": "verified_conference", "publication_year": 2024, "venue_short_name": "ACL"}, 2024, 2026))
        self.assertFalse(is_verified_in_range({"status": "needs_manual_review", "publication_year": 2024, "venue_short_name": "ACL"}, 2024, 2026))
        self.assertFalse(is_verified_in_range({"status": "verified_conference", "publication_year": 2027, "venue_short_name": "ACL"}, 2024, 2026))

    def test_openalex_cannot_be_the_conference_confirmation_source(self):
        venues = load_venues(ROOT / "venues.json")
        evidence, venue = choose_conference_evidence(
            [{"provider": "OpenAlex", "matched": True, "source": "Proceedings of ACL 2026", "authors": "A"}], venues
        )
        self.assertIsNone(evidence)
        self.assertIsNone(venue)


if __name__ == "__main__":
    unittest.main()
