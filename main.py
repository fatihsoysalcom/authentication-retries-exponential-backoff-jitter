import time
import random

# Simulate an authentication service that sometimes fails
# and takes a variable amount of time.
# This service will fail more often initially to demonstrate retry necessity.
SERVICE_FAILURE_RATE = 0.6  # 60% chance of failure initially
SERVICE_RESPONSE_TIME_MIN = 0.1
SERVICE_RESPONSE_TIME_MAX = 0.5

def simulated_auth_service(attempt_count):
    """Simulates an authentication attempt. Returns True on success, False on failure."""
    print(f"  [Service] Received request (attempt {attempt_count})...")
    time.sleep(random.uniform(SERVICE_RESPONSE_TIME_MIN, SERVICE_RESPONSE_TIME_MAX))

    # Make the service more likely to succeed after a few attempts
    # to simulate recovery or transient issues.
    adjusted_failure_rate = max(0.1, SERVICE_FAILURE_RATE - (attempt_count * 0.1))

    if random.random() < adjusted_failure_rate:
        print(f"  [Service] Authentication FAILED (failure rate: {adjusted_failure_rate:.2f}).")
        return False
    else:
        print(f"  [Service] Authentication SUCCESS (failure rate: {adjusted_failure_rate:.2f}).")
        return True

def client_no_retry():
    """Attempts authentication once. Fails if the service is unavailable."""
    print("\n--- Client: No Retry Strategy ---")
    print("Attempting authentication without retries...")
    if simulated_auth_service(1):
        print("Authentication successful on first try!")
    else:
        print("Authentication failed. No retry attempted.")

def client_naive_retry(max_retries=3, fixed_delay_seconds=1):
    """Attempts authentication with a fixed delay between retries. Can overwhelm service."""
    print(f"\n--- Client: Naive Retry Strategy (max {max_retries} retries, {fixed_delay_seconds}s delay) ---")
    for i in range(1, max_retries + 2): # +1 for initial attempt
        print(f"Attempt {i} of {max_retries + 1}...")
        if simulated_auth_service(i):
            print(f"Authentication successful after {i} attempts.")
            return
        if i <= max_retries: # Don't delay after final failed attempt
            print(f"Authentication failed. Retrying in {fixed_delay_seconds} second(s)...")
            time.sleep(fixed_delay_seconds)
    print("Authentication failed after all retries.")

def client_exponential_backoff_retry(max_retries=5, initial_delay_seconds=0.5, max_delay_seconds=8):
    """Attempts authentication with exponential backoff and jitter for resilience."""
    print(f"\n--- Client: Exponential Backoff Retry Strategy (max {max_retries} retries) ---")
    delay = initial_delay_seconds
    for i in range(1, max_retries + 2): # +1 for initial attempt
        print(f"Attempt {i} of {max_retries + 1}...")
        if simulated_auth_service(i):
            print(f"Authentication successful after {i} attempts.")
            return

        if i <= max_retries:
            # Apply jitter: add a random fraction to the delay to prevent thundering herd
            jitter = random.uniform(0, delay * 0.5) # Jitter up to 50% of current delay
            sleep_time = min(delay + jitter, max_delay_seconds)
            print(f"Authentication failed. Retrying in {sleep_time:.2f} second(s) (base delay: {delay:.2f}, jitter: {jitter:.2f})...")
            time.sleep(sleep_time)
            # Exponentially increase the base delay
            delay = min(delay * 2, max_delay_seconds)

    print("Authentication failed after all retries.")

if __name__ == "__main__":
    print("Simulating an authentication service with varying reliability...")
    print("------------------------------------------------------------------")

    client_no_retry()
    client_naive_retry()
    client_exponential_backoff_retry()

    print("\n------------------------------------------------------------------")
    print("Demonstration complete. Observe how different retry strategies affect success and system load.")
