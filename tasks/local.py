from pathlib import Path

from jinja2 import Environment, FileSystemLoader, Template


def template(c, source_path, target_path, context=None):
    source_path = Path(source_path)
    target_path = Path(target_path)
    j2env = Environment(
        loader=FileSystemLoader(f'{source_path.parent}'),
        keep_trailing_newline=True
    )
    j2env.get_template(f'{source_path.name}').stream(**context or {}).dump(f'{target_path}')


def content(c, content, target_path, context=None):
    target_path = Path(target_path)
    Template(content).stream(**context or {}).dump(f'{target_path}')
