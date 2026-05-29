n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

result = dict()
for cmd in commands:
    if cmd[0] == "add":
        result[cmd[1]] = cmd[2]
    elif cmd[0] == "find":
        if cmd[1] in result.keys():
            print(result[cmd[1]])
        else:
            print("None")
    elif cmd[0] == "remove":
        result.pop(cmd[1])