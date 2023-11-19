import threading
import time
import winsound

class AlertQueue:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()

    def add_alert(self, recommendation):
        with self.lock:
            self.queue.append(recommendation)

    def show_alerts(self):
        while True:
            with self.lock:
                if not self.queue:
                    break

            recommendation = self.queue.pop(0)
            # Display the recommendation as a popup or notification
            print(recommendation)

            # Play a sound alert
            winsound.Beep(440, 500)

            # Add a delay between alerts
            time.sleep(2)

alert_queue = AlertQueue()

def start_alert_thread():
    alert_thread = threading.Thread(target=alert_queue.show_alerts)
    alert_thread.daemon = True  # Set as daemon thread to terminate with the main program
    alert_thread.start()

def add_alert(recommendation):
    alert_queue.add_alert(recommendation)