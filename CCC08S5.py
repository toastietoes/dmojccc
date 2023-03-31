#a num of particles are put into a reactor
#they alternate turns, Patrick always first
#player must select any remaning particles to form a possible reaction
#particles will be destroyed after until no reactions can be formed
#the first person unable to form a reaction loses

n = int(input())

for i in range(n):
    a, b, c, d = map(int, input().split())
    