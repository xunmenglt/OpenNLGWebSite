import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from publication_lib import classify_venue, load_venues

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = Path(__file__).with_name("fixtures") / "profile.html"


class ExtractScholarTests(unittest.TestCase):
    def test_extracts_only_whitelisted_conference_in_range(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            subprocess.run(
                [sys.executable, str(ROOT / "extract_scholar.py"), "--input", str(FIXTURE), "--output-dir", str(output)],
                check=True,
                capture_output=True,
                text=True,
            )
            candidates = json.loads((output / "candidates.json").read_text(encoding="utf-8"))
            rejected = json.loads((output / "rejected.json").read_text(encoding="utf-8"))
        self.assertEqual(1, len(candidates))
        self.assertEqual("ACL", candidates[0]["venue_short_name"])
        self.assertEqual("ACL2025", candidates[0]["venue_label"])
        self.assertEqual(2, len(rejected))

    def test_uses_explicit_conference_year_over_scholar_year(self):
        fixture = ROOT / "tests" / "fixtures" / "conference-year.html"
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            subprocess.run(
                [sys.executable, str(ROOT / "extract_scholar.py"), "--input", str(fixture), "--output-dir", str(output)],
                check=True,
                capture_output=True,
                text=True,
            )
            candidates = json.loads((output / "candidates.json").read_text(encoding="utf-8"))
        self.assertEqual(2026, candidates[0]["publication_year"])
        self.assertEqual("ACL2026", candidates[0]["venue_label"])

    def test_recognises_long_form_acl_inlg_and_coling_sources(self):
        venues = load_venues(ROOT / "venues.json")
        self.assertEqual("ACL", classify_venue("Proceedings of the 64th Annual Meeting of the Association for Computational ", venues))
        self.assertEqual("INLG", classify_venue("The 18th International Natural Language Generation Conference (INLG 2025)", venues))
        self.assertEqual("COLING", classify_venue("Proceedings of the 31st International conference on computational ", venues))


if __name__ == "__main__":
    unittest.main()
