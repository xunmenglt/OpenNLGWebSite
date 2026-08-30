import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from resolve_official_pdfs import direct_pdf_from_url


class OfficialPdfResolverTests(unittest.TestCase):
    def test_acl_doi_maps_to_anthology_pdf(self):
        self.assertEqual(
            "https://aclanthology.org/2025.acl-long.263.pdf",
            direct_pdf_from_url("https://doi.org/10.18653/v1/2025.acl-long.263"),
        )

    def test_openreview_forum_maps_to_pdf(self):
        self.assertEqual(
            "https://openreview.net/pdf?id=abc123",
            direct_pdf_from_url("https://openreview.net/forum?id=abc123"),
        )

    def test_neurips_abstract_maps_to_paper_pdf(self):
        self.assertEqual(
            "https://proceedings.neurips.cc/paper_files/paper/2025/file/hash-Paper-Conference.pdf",
            direct_pdf_from_url("https://proceedings.neurips.cc/paper_files/paper/2025/file/hash-Abstract-Conference.html"),
        )

    def test_unknown_url_is_not_converted(self):
        self.assertEqual("", direct_pdf_from_url("https://example.org/paper"))


if __name__ == "__main__":
    unittest.main()
