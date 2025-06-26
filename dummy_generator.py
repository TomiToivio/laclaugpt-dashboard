import pandas as pd
import json
import random
import datetime

def create_random_date():
    """Generate a random date within the last year."""
    start_date = datetime.datetime.now() - datetime.timedelta(days=365)
    end_date = datetime.datetime.now()
    return start_date + (end_date - start_date) * random.random()

def create_random_username():
    """Generate a random username."""
    return f"user_{random.randint(1, 1000)}"

