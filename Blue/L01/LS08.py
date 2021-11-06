def getChar(x):
    return chr(x + ord('a'))

s = input()
t = input()

need_tree = array = automaton = False

for i in range(26):
    t_count = t.count(getChar(i))
    s_count = s.count(getChar(i))

    if t_count > s_count:
        need_tree = True
    elif t_count < s_count:
        automaton = True

index_found, match = 0, -1

for i in range(len(t)):
    index_found = s.find(t[i], match + 1)
    if index_found > match:
        match = index_found
    else:
        array = True
        break

if need_tree:
    print("need tree")
elif automaton and array:
    print("both")
elif automaton:
    print("automaton")
else:
    print("array")