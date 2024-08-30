global_state = {
    "name": "Global State",
    "notes": "",
    "variables": [
        {
            "type": "Entity Type",
            "name": "Dummy",
            "description": "The dummy entity",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Qi Type",
            "name": "Qi Supply",
            "description": "The total supply of Qi",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Quai Type",
            "name": "Quai Supply",
            "description": "The total supply of Quai",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Qi Type",
            "name": "Locked Qi Supply",
            "description": "The total supply of Qi that is locked",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Quai Type",
            "name": "Locked Quai Supply",
            "description": "The total supply of Quai that is locked",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Block Number Type",
            "name": "Block Number",
            "description": "The current block that the system is on",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Block Difficulty Type",
            "name": "Block Difficulty",
            "description": "The latest difficulty for blocks",
            "symbol": None,
            "domain": None,
        },
        # {
        #     "type": "Hash Type",
        #     "name": "Current Hash Difference",
        #     "description": "",
        #     "symbol": None,
        #     "domain": None,
        # },
        {
            "type": "Conversions Array Type",
            "name": "Historical Converted Qi",
            "description": "An array of the conversions from Qi to Quai. The Qi Values will be negative in each entry and Quai values will be positive. Time is also logged in the entries of the array.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Conversions Array Type",
            "name": "Historical Converted Quai",
            "description": "An array of the conversions from Quai to Qi. The Quai Values will be negative in each entry and Qi values will be positive. Time is also logged in the entries of the array.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Mined Ratio Array Type",
            "name": "Historical Mined Ratio",
            "description": "An array of the historical ratios of mining between Qi and Quai which the miners had chosen at given times. 0 corresponds to 100% Qi, 1 corresponds to 100% Quai, number in between are the increments between those balances.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Hash Array Type",
            "name": "Historical Qi Hash",
            "description": "An array of the historical amount of hash attributed to Qi in block rewards with block numbers attatched to each entry.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Hash Array Type",
            "name": "Historical Quai Hash",
            "description": "An array of the historical amount of hash attributed to Quai in block rewards with block numbers attatched to each entry.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Gain Type",
            "name": "K Qi",
            "description": "The controller coeffecient for Qi.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Gain Type",
            "name": "K Quai",
            "description": "The controller coeffecient for Quai.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "USD Type",
            "name": "Quai Price",
            "description": "The current price of Quai.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "USD Type",
            "name": "Qi Price",
            "description": "The current price of Qi.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Simulation History Log Type",
            "name": "Simulation History Log",
            "description": "The logged data from simulation history.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Number of Regions Type",
            "name": "Number of Regions",
            "description": "The current number of regions.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Zones per Region Type",
            "name": "Zones per Region",
            "description": "The current number of zones in each region.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Datetime Type",
            "name": "Time",
            "description": "The current time in the system.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Delta Time Type",
            "name": "Delta Time",
            "description": "The amount of time covered in the current simulation epoch.",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Unlock Schedule Type",
            "name": "Quai Unlock Schedule",
            "description": "The schedule of Quai token unlocks that will happen in the future",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Unlock Schedule Type",
            "name": "Qi Unlock Schedule",
            "description": "The schedule of Qi token unlocks that will happen in the future",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Mining Beta Vector Type",
            "name": "Population Mining Beta Vector",
            "description": "The population betas, not known to the controller",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Mining Beta Vector Type",
            "name": "Estimated Mining Beta Vector",
            "description": "The controllers current estimation of the beta vector",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Logistic Classifier Type",
            "name": "Logistic Classifier",
            "description": "The logistic classifier used for beta estimation",
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Simulation History Log Type",
            "name": "Mining Log",
            "description": "The log of mined blocks",
            "symbol": None,
            "domain": None,
        },
    ],
}
