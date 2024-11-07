#!/usr/bin/env python3
"""Module for validating hashed passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt. Parameters: password (str): The password to hash. Returns: bytes: The hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates a password against a hashed password using bcrypt. Parameters: hashed_password (bytes): The hashed password. password (str): The password to validate. Returns: bool: True if the password matches the hash, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
