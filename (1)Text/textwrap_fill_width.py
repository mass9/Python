import textwrap
from textwrap_example import sample_text

#dedented text can be passed through fill() with a few values 

dedented_text = textwrap.dedent(sample_text).strip()

for width in [45, 60]:
    print('{} Columns:\n'.format(width))
    print(textwrap.fill(dedented_text , width = width ))
    print()
