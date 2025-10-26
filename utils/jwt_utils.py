import jwt, os
from dotenv import load_dotenv
from jwt.exceptions import InvalidTokenError

load_dotenv()

def decode_token(token):
    try:
        return jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
    except InvalidTokenError:
        return None
