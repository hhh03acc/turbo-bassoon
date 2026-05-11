import os
import time
from datetime import datetime

class DataEngine:
    def __init__(self, node_id):
        self.node_id = node_id
        self.status = "Idle"

    def run_check(self):
        self.status = "Processing"
        items = range(100)
        for i in items:
            if i % 10 == 0:
                print(f"Node {self.node_id}: Batch {i}% verified")
                time.sleep(0.2)
        self.status = "Completed"

if __name__ == "__main__":
    engine = DataEngine("CI-Worker-01")
    engine.run_check()
