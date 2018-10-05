import textwrap

from textwrap_example import sample_text

"""
This script present the preview or the summary of the text
"""
dedented_text = textwrap.dedent(sample_text)

original = textwrap.fill(dedented_text, width=50)\

print('Original: \n')
print(original)

shortened = textwrap.shorten(original, 100)
shortened_wrapped = textwrap.fill(shortened, width=50)

print('\nShorteded:\n')
print(shortened_wrapped)
