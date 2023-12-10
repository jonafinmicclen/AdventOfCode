IDENTIFIERS = ['0','1','2','3','4','5','6','7','8','9','zero','one','two','three','four','five','six','seven','eight','nine']
IDENTITIES = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]

input = open('.\Day 1 Input' ,'r')

result = 0

for line in input:

    line = line.lower()

    leftIdentities = []
    rightIdentities = []

    for identifier in zip(IDENTIFIERS,IDENTITIES):
        try:
            leftIdentities.append([line.index(identifier[0]), identifier[1]])
            rightIdentities.append([line.rindex(identifier[0]), identifier[1]])
        except:
            pass

    identity_index, identity = zip(*leftIdentities)
    l = identity[identity_index.index(min(identity_index))] * 10

    identity_index, identity = zip(*rightIdentities)
    r = identity[identity_index.index(max(identity_index))]

    print(l+r, line)

    result +=  l+r

print(result)