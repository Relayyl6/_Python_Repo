# Example using Python's built-in hash() function
data = "Hello, World!"

# Get the hash value (integer)
hash_value = hash(data)

print(f"Data: {data}")
print(f"Hash value (built-in): {hash_value}")


def simple_hash(input_string):
    """A simple custom hash function for strings."""
    hash_value = 0
    for char in input_string:
        # Convert character to ASCII value, scale, and mix
        hash_value = (hash_value * 31 + ord(char)) % (2 ** 32)  # Modulo to limit size
    return hash_value

# Example usage
data = "Hello, World!"
custom_hash = simple_hash(data)

print(f"Data: {data}")
print(f"Custom hash value: {custom_hash}")