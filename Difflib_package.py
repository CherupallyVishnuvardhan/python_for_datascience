import difflib

fline='Hello. How are you? I am fine.'
glines='How are you, Lillian? I am doing well.'

d=difflib.Differ()
diff=d.compare(fline,glines)

print(diff)
for line in diff:
    print(line)