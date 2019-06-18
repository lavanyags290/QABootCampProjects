print("""
There's going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

str = """
There's going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

line = str.split('\n')
for i in range(len(line)):
    line[i] = line[i].replace(line[i], "?")
    print(line[i])
