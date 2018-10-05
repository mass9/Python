import textwrap
from textwrap_example import sample_text
"""
This script will present the indented for the selected text
"""
dedented_text = textwrap.dedent(sample_text).strip()

print(textwrap.fill(dedented_text,
initial_indent='',
subsequent_indent=' ' * 4,
width=50,
))
