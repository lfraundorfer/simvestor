class HistoryTracker:
    """Records and provides daily snapshots of portfolio balances."""
    def __init__(self):
        self.records = []

    def record(self, day: int, balances: dict):
        # Copy the balances to avoid mutation issues
        self.records.append({"day": day, **balances})

    def get_records(self):
        return self.records