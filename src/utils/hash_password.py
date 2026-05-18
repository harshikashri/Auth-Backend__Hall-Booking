import hashlib
import hmac
import os


def hash_password(password: str) -> str:
    """Hash a plain password using PBKDF2-HMAC-SHA256 and return a string token.

    Format: pbkdf2_sha256$<iterations>$<salt_hex>$<hash_hex>
    """
    salt = os.urandom(16)
    iterations = 210000
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        iterations,
    )
    return f"pbkdf2_sha256${iterations}${salt.hex()}${password_hash.hex()}"


def verify_password(plain_password: str, stored_password_hash: str) -> bool:
    """Verify plain password against stored PBKDF2 hash token."""
    try:
        algorithm, iterations_str, salt_hex, hash_hex = stored_password_hash.split("$")
        if algorithm != "pbkdf2_sha256":
            return False

        iterations = int(iterations_str)
        salt = bytes.fromhex(salt_hex)
        expected_hash = bytes.fromhex(hash_hex)

        computed_hash = hashlib.pbkdf2_hmac(
            "sha256",
            plain_password.encode("utf-8"),
            salt,
            iterations,
        )
        return hmac.compare_digest(computed_hash, expected_hash)
    except (ValueError, TypeError):
        return False