from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate_skills import validate


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / 'example' / 'SKILL.md'
        self.skill.parent.mkdir()
        self.skill.write_text('---\nname: example\ndescription: 学习辅导\n---\n', encoding='utf-8')

    def test_valid_reference(self):
        (self.skill.parent / 'reference.md').write_text('材料', encoding='utf-8')
        with self.skill.open('a', encoding='utf-8') as f:
            f.write('[参考](reference.md)\n[外部](https://example.com)\n')
        self.assertEqual(validate(self.root), [])

    def test_broken_reference_fails(self):
        with self.skill.open('a', encoding='utf-8') as f:
            f.write('[参考](missing.md)')
        self.assertTrue(any('missing.md' in e for e in validate(self.root)))

    def test_wrong_name_fails(self):
        self.skill.write_text('---\nname: other\ndescription: test\n---\n', encoding='utf-8')
        self.assertTrue(any('match directory' in e for e in validate(self.root)))

    def test_empty_description_fails(self):
        self.skill.write_text('---\nname: example\ndescription: ""\n---\n', encoding='utf-8')
        self.assertTrue(any('description' in e for e in validate(self.root)))

    def test_empty_repository_fails(self):
        self.skill.unlink()
        self.assertEqual(validate(self.root), ['No skill directories found'])


if __name__ == '__main__':
    unittest.main()
