import time
import itertools
import string
from multiprocessing import Pool, cpu_count


def verify_password(password, correct_password):
    return password == correct_password


def try_password(attempt):
    password_attempt, correct_password = attempt
    if verify_password(password_attempt, correct_password):
        return password_attempt
    return None


def brute_force_password(correct_password, max_length=10):
    characters = string.ascii_lowercase + string.digits
    found_password = None

    pool = Pool(cpu_count())
    try:
        for length in range(1, max_length + 1):
            if found_password:
                break
            attempts = itertools.product(characters, repeat=length)
            for result in pool.imap_unordered(
                try_password,
                (("".join(password), correct_password) for password in attempts),
            ):
                if result:
                    found_password = result
                    break
    finally:
        pool.close()
        pool.join()

    return found_password


def main():
    correct_password = "aaabbb"
    start_time = time.time()

    found_password = brute_force_password(correct_password)

    end_time = time.time()
    elapsed_time = end_time - start_time

    if found_password:
        print(f"Password found: {found_password}")
        print(f"Elapsed time: {elapsed_time:.6f} s")
    else:
        print("Password not found")


if __name__ == "__main__":
    main()
