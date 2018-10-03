# Used to remove left indentation

import textwrap

from textwarp_example import sample_text

dedented_text = textwrap.dedent(sample_text)
print('Dedented: ')
print(dedented_text)
