"""Validate skill metadata and local Markdown file references; no network access."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


def validate(root: Path) -> list[str]:
    errors = []
    skills = sorted(root.glob('*/SKILL.md'))
    if not skills:
        return ['No skill directories found']
    for skill in skills:
        try:
            text = skill.read_text(encoding='utf-8-sig')
            match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
            if not match:
                raise ValueError('missing YAML frontmatter')
            meta = yaml.safe_load(match.group(1))
            if not isinstance(meta, dict):
                raise ValueError('frontmatter must be a mapping')
            name = meta.get('name')
            if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
                raise ValueError('invalid skill name')
            if len(name) > 64 or name != skill.parent.name:
                raise ValueError('name must match directory and have at most 64 characters')
            description = meta.get('description')
            if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                raise ValueError('description must contain 1-1024 characters')
        except (ValueError, UnicodeError, yaml.YAMLError) as exc:
            errors.append(f'{skill.relative_to(root)}: {exc}')
    # Validate references in source skills and maintained root docs only.
    documents = [p for s in skills for p in s.parent.rglob('*.md')]
    documents += [root / n for n in ('README.md', 'CHANGELOG.md', 'AGENTS.md') if (root / n).exists()]
    for document in documents:
        try:
            text = document.read_text(encoding='utf-8-sig')
        except UnicodeError:
            errors.append(f'{document.relative_to(root)}: not UTF-8')
            continue
        # This check covers inline Markdown file links, not remote availability or anchors.
        for destination in re.findall(r'\]\(([^)\n]+)\)', text):
            destination = destination.strip().strip('<>')
            parsed = urlsplit(destination)
            if parsed.scheme or destination.startswith(('#', '//')):
                continue
            target = (document.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(root.resolve()) or not target.exists():
                errors.append(f'{document.relative_to(root)}: missing or external local target {destination}')
    return errors


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    for error in errors:
        print(error)
    if errors:
        sys.exit(1)
    print(f'Validated {len(list(root.glob("*/SKILL.md")))} skills and local Markdown references.')
