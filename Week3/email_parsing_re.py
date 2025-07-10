import re
email = "Tharun.20231cbd0034@presidencyuniversity.com"
match = re.search(r"^(\w+)\.(\w+)@(\w+)\.\w+", email)
try:
    print("Name  : ", match.group(1))
    print("Roll number: ",match.group(2))
    print("Clg name: ",match.group(3))
except:
    print("Nil")