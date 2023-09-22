import time
from .. import accessories

accs = accessories.Accessories()

# Initial text
initial_text = "This is some initial text."
accs.print_and_update(initial_text, len(initial_text))
time.sleep(2)  # Delay to simulate an update

# Updated text
updated_text = "This is the updated text."
accs.print_and_update(updated_text, len(initial_text))