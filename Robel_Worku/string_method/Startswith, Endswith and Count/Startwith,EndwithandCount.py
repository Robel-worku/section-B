txt = "this the new sentence"

print(txt.startswith("this"))        # true
print(txt.startswith("the"))         # false

print(txt.endswith("sentence"))       # true
print(txt.endswith("the"))            # false



print(txt.count("e"))        # 5 instances found
print(txt.count("q"))        # 0
