import signal
import time

def handle_signal(signum, frame):
    print(f"Received signal: {signum}")
    # Дополнительные действия, которые вы хотите выполнить при получений сигнала

# Привязка оброботчика к сигналу SIGINT
signal.signal(signal.SIGINT, handle_signal)

print("Waiting for a signal ...")
while True:
    time.sleep(1)
