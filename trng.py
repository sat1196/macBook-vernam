import os
import time
import hashlib

def generate_noise(output_length=1024):
    """Generate pseudo-random noise based on disk I/O timings.

    Args:
        output_length (int): Length of the noise string to produce.

    Returns:
        str: A string of '0's and '1's representing the generated noise.
    """
    noise = []
    for _ in range(output_length):
        start_time = time.time()
        # Perform a disk I/O operation. Here, we're just reading from the current directory.
        os.listdir('.')
        end_time = time.time()

        # Use the timing of the operation as a source of entropy
        elapsed_time = end_time - start_time
        hash_digest = hashlib.sha256(str(elapsed_time).encode()).digest()

        # Convert the hash digest to a binary string and take the last bit
        bit = bin(int.from_bytes(hash_digest, 'big'))[-1]
        noise.append(bit)

    return ''.join(noise)
