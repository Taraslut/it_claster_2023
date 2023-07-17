import re
from collections import Counter

text = """
A ChainMap groups multiple dicts or other mappings together to create a single, updateable view. If no maps are specified, a single empty dictionary is provided so that a new chain always has at least one mapping.
The underlying mappings are stored in a list. That list is public and can be accessed or updated using the maps attribute. There is no other state.
Lookups search the underlying mappings successively until a key is found. In contrast, writes, updates, and deletions only operate on the first mapping.
A ChainMap incorporates the underlying mappings by reference. So, if one of the underlying mappings gets updated, those changes will be reflected in ChainMap.
All of the usual dictionary methods are supported. In addition, there is a maps attribute, a method for creating new subcontexts, and a property for accessing all but the first mapping:"""

text = text.lower()
words = re.split(r"\s", text)

# d_count = {}
#
#
# for word in words:
#     if word not in d_count:
#         d_count[word] = 1
#     else:
#         d_count[word] += 1
#
# print(d_count)
#
# m = max(d_count.values())
#
# for word in d_count:
#     if m == d_count[word]:
#         print(word)

count = Counter(words)

print(count.most_common(1)[0][0])