# Split a string with multiple delimiters in Python

import re

# 👇️ split string with 2 delimiters

my_str = 'bobby,hadz-dot,com'

my_list = re.split(r',|-', my_str)  # 👈️ split on comma or hyphen

print(my_list)  # 👉️ ['bobby', 'hadz', 'dot', 'com']