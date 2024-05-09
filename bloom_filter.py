import hashlib

def hash_functions(item, num_hashes, size):
    result = []
    for i in range(num_hashes):
        hash_obj = hashlib.sha256()  # cryptographic hash functions SHA-256 
        hash_obj.update(item.encode('utf-8') + str(i).encode('utf-8'))
        result.append(int(hash_obj.hexdigest(), 16) % size)
    return result


class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bit_array = [0] * size

    def add(self, item):
        index = hash_functions(item) % self.size
        self.bit_array[index] = 1

    def check(self, item):
        index = hash(item) % self.size
        return self.bit_array[index] == 1
    # Add check for false positive rate against size
    # Add check false positive rate if size was exceeded
    # Add check for compression rate (false positive rate vs expected false positive rate)

# Example 
bloom = BloomFilter(10)  # just for demostration

bloom.add("apple")
bloom.add("banana")

# Check for existing and non-existing items
print("banana", bloom.check("banana"))  # Should be True
print("cherry", bloom.check("cherry"))  # Should be False

# Example 2 - Testing Different Data Type
bloom = BloomFilter(10)

bloom.add("TTAATTA")
bloom.add("ATTACTC")

# Check for existing and non-existing items
print("TTAATTA", bloom.check("TTAATTA"))  # Should be True
print("ATTACTC", bloom.check("ATTACTC"))  # Should be True
print("ACTCAC", bloom.check("ACTCAC"))  # Should be False
