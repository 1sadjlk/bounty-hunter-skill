import sys

# A script to check payout status via platform APIs or simple web scraping (simulated)

def check_status(task_id):
    # Simulated check
    return "PENDING"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        status = check_status(sys.argv[1])
        print(f"Status for {sys.argv[1]}: {status}")
    else:
        print("Usage: python3 check_payouts.py <task_id>")
