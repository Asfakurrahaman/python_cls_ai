from collections import deque
bank = deque(['asfak','anis','karim'])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()

if not bank:
    print('No parson Left')