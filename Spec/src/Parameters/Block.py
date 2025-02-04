mining_parameter_set = {
    "name": "Mining Parameter Set",
    "notes": "The parameters related to the mining",
    "parameters": [
        {
            "variable_type": "Block Difficulty Multiples Type",
            "name": "Block Difficulty Multiples",
            "description": "The difficulty of different levels of blocks as multipliers on global difficulty",
            "symbol": None,
            "domain": None,
            "parameter_class": "System",
        },
        {
            "variable_type": "Seconds Type",
            "name": "Target Mining Time",
            "description": "The target time for mining to take",
            "symbol": None,
            "domain": None,
            "parameter_class": "System",
        },
        {
            "variable_type": "Integer Type",
            "name": "Quai Reward Base Parameter",
            "description": "The base used for Quai reward computation",
            "symbol": "B",
            "domain": None,
            "parameter_class": "System",
        },
        {
            "variable_type": "Hash Array Type",
            "name": "Aggregate Hashpower Series",
            "description": "A series of the aggregate hashpower to be used at each block number",
            "symbol": None,
            "domain": None,
            "parameter_class": "Behavioral",
        },
        {
            "variable_type": "Integer Type",
            "name": "Difficulty Adjustment Period",
            "description": "The number of blocks over which difficulty is adjusted",
            "symbol": None,
            "domain": None,
            "parameter_class": "System",
        },
        {
            "variable_type": "Float Type",
            "name": "Difficulty Randomness Sigma",
            "description": "The mean value for randomness percentage multiplied into block difficulties (1 being default/average equal to block difficulty)",
            "symbol": None,
            "domain": None,
            "parameter_class": "System",
        },
        {
            "variable_type": "Float Type",
            "name": "Difficulty Randomness Mu",
            "description": "The standard deviation of the percentage multiplied into block difficulties",
            "symbol": None,
            "domain": None,
            "parameter_class": "System",
        },
        {
            "variable_type": "Float Type",
            "name": "Probability of Rational Miners",
            "description": "The probability that a given miner is going to act rationally.",
            "symbol": None,
            "domain": "[0, 1]",
            "parameter_class": "Behavioral",
        },
    ],
}


block_parameter_sets = [mining_parameter_set]
