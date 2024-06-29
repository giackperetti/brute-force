import time


def verify_pin(pin, pin_corretto):
    return pin == pin_corretto


def brute_force_pin(pin_corretto):
    for i in range(1000000):
        pin_tentativo = f"{i:06d}"
        if verify_pin(pin_tentativo, pin_corretto):
            return pin_tentativo
    return None


def main():
    pin_corretto = "712304"
    start_time = time.time()

    pin_trovato = brute_force_pin(pin_corretto)

    end_time = time.time()
    elapsed_time = end_time - start_time

    if pin_trovato:
        print(f"PIN code found: {pin_trovato}")
        print(f"Elapsed time: {elapsed_time:.6f} s")
    else:
        print("PIN not found")


if __name__ == "__main__":
    main()
