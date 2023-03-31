import hashlib, datetime
from multiprocessing import Pool

def check_hash(i, hash_value):
    if hashlib.md5(str(i).encode()).hexdigest() == hash_value:
        return i

if __name__ == "__main__":
    starttime = datetime.datetime.now()
    hash_value = "cf949da80bf4b87641b5896d8786a2b6"

    with Pool() as p:
        result = p.starmap(check_hash, [(i, hash_value) for i in range(1000000, 10000000)])

    result = list(filter(None, result))
    if result:
        print(f"The 7-digit number with the MD5 hash value {hash_value} is: {result[0]}")
        endtime = datetime.datetime.now()
        print(endtime - starttime)
    else:
        print("No matching number found.")