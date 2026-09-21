"""All independently distributed skills must use the same state contract."""
from pathlib import Path
import unittest


class StateDistributionTests(unittest.TestCase):
    def test_portable_contracts_match(self):
        root = Path(__file__).resolve().parents[1]
        for relative in ('references/state-protocol.md', 'templates/learning-state.md'):
            with self.subTest(file=relative):
                canonical = root / 'personal-learning-skill' / relative
                for name in ('learning-method-skill', 'scientific-thinking-skill'):
                    with self.subTest(skill=name):
                        distributed = root / name / relative
                        self.assertEqual(canonical.read_bytes(), distributed.read_bytes())


if __name__ == '__main__':
    unittest.main()
