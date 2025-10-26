from utils.jwt_utils import decode_token
from dotenv import load_dotenv
import os

load_dotenv()

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ0ZXN0QGV4YW1wbGUuY29tIn0.WTfordv17oLJJd0cgArNhO-GcpNFKFTP7nMHWdYMce8"

print(" SECRET_KEY =", os.getenv("SECRET_KEY"))
print(" TOKEN =", token)
print(" TOKEN PART COUNT =", len(token.split(".")))

payload = decode_token(token)

print(" Payload:", payload)
