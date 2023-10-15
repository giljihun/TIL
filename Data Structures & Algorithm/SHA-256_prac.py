import hashlib

target1 = "giijihun"
result1 = hashlib.sha256(target1.encode()).hexdigest()
print("Result of Hashing - [giljihun] : ",result1)

target2 = "giijihun!"
result2 = hashlib.sha256(target2.encode()).hexdigest()
print("Result of Hashing - [giljihun!] : ",result2)

target3 = 'a'
binary1 = ' '.join(format(ord(c), 'b') for c in target3)

print(binary1)