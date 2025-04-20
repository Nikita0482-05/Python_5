import random as r
import json
import string


n = r.choice(string.ascii_uppercase) + ''.join(r.choices(string.ascii_lowercase, k=r.randint(3, 8)))
ln = r.choice(string.ascii_uppercase) + ''.join(r.choices(string.ascii_lowercase, k=r.randint(5, 12)))


nm = f"{n} {ln}"
a = r.randint(18, 80)
e = ''.join(r.choices(string.ascii_lowercase + string.digits, k=10)) + "@mail.com"
p = ''.join(r.choices(string.ascii_letters + string.digits + string.punctuation, k=12))


d = {"name": nm, "age": a, "email": e, "password": p}
with open("user.json", "w") as f:
    json.dump(d, f, indent=4)

with open("user.json") as f:
    print(f.read())