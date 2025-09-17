from werkzeug.security import generate_password_hash
print(generate_password_hash('password', method='pbkdf2:sha256', salt_length=8))
#This will generate a hashed password for 'password' using PBKDF2 with SHA-256 and a salt length of 8.
