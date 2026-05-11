import os

def clean_logs():
    log_dir = "./logs"
    if os.path.exists(log_dir):
        for file in os.listdir(log_dir):
            os.remove(os.path.join(log_dir, file))
        print("Log directory cleaned.")

if __name__ == "__main__":
    clean_logs()
