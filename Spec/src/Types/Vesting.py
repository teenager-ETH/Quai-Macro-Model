VestingScheduleType = {
    "name": "Vesting Schedule Type",
    "type": "VestingScheduleType",
    "notes": "A list of objects with the following attributes: vesting_amount, vesting_frequency, recipient, time (in years) for when it is active, and optionally duration if the vesting_frequency is not immediate",
}

UnlockScheduleType = {
    "name": "Unlock Schedule Type",
    "type": "UnlockScheduleType",
    "notes": "A sorted list (by earliest time) where each list object has the time for unlocking (in years), the amount, and the recipient",
}


vesting_types = [VestingScheduleType, UnlockScheduleType]