a = int(input())
b = [int(elem) for elem in input().split(" ")]
c = [int(elem) for elem in input().split(" ")]

print(*[x*a for x in b], *[x*a for x in c])