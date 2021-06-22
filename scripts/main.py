from datetime import datetime
import os

print("PRINT FROM PYTHON: ACTION 1.2 - STARTED")

print(os.getenv['INPUT_USER_VALUE'])
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('log.md', 'w') as f:
    f.write(f'# {timestamp} {INPUT_USER_VALUE}')
    
print("PRINT FROM PYTHON: ACTION 1.2 - COMPLETED")
