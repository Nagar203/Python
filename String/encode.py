s = "THI$ !s $TR!ng. encode å"

print(s.encode())

print(s.encode(encoding="ascii",errors="backslashreplace"))
print(s.encode(encoding="ascii",errors="ignore"))
print(s.encode(encoding="ascii",errors="namereplace"))
print(s.encode(encoding="ascii",errors="replace"))
print(s.encode(encoding="ascii",errors="xmlcharrefreplace"))