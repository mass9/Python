"""
Characer set is a group of character, any one of which can match the patterns
"""

from re_test_patterns import test_patterns

test_patterns(
'abbaabbba',
[('[ab]', 'either a or b'),
('a[ab]+', 'a followed by 1 or more a or b'),
('a[ab]+?', 'a followed by 1 or more a or b, not greedy')],
)
