s = "The quick brown fox jumps over the lazy dog"
for r in (("brown", "lazy"), ("lazy", "quick")):
    s = s.replace(*r)

print(s)