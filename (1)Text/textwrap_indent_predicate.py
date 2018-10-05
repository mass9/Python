import textwrap

from textwrap_example import sample_text

# Controlling which lines receive the new prefix
def should_indent(line):
    print('Indent {!r} ? '.format(line))
    return len(line.strip()) % 2 == 0

dedented_text =textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width =50)

#It will add the prefix EVEN to lines that contain an even number of characters.

final = textwrap.indent(wrapped, 'EVEN', predicate = should_indent)

print("\nQuoted Blocks : \n")
print(final)
