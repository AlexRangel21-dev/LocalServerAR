from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

passwords = [
    "Alex123",
    "Arcadia123"
]

for password in passwords: 
    print (f"{password} -> {pwd_context.hash(password)}")
    