if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        line = input()
        if (line == 'print'):
            print(list)
        elif (line == 'pop'):
            list.pop()
        elif (line == 'sort'):
            list.sort()
        elif (line == 'reverse'):
            list.reverse()
        elif (line.startswith('append')):
            cmd, val = line.split(' ')
            list.append(int(val))
        elif (line.startswith('remove')):
            cmd, val = line.split(' ')
            list.remove(int(val))
        elif (line.startswith('insert')):
            cmd, ind, val = line.split(' ')
            list.insert(int(ind), int(val))

