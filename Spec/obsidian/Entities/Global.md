## Notes

## State
### Notes

### Variable Table
| Name | Description | Type | Symbol | Domain |
| --- | --- | --- | --- | --- |
|[[Global State-Dummy\|Dummy]]|The dummy entity|[[Entity Type]]|||
|[[Global State-Qi Supply\|Qi Supply]]|The total supply of Qi|[[Qi Type]]|||
|[[Global State-Quai Supply\|Quai Supply]]|The total supply of Quai|[[Quai Type]]|||
|[[Global State-Block Number\|Block Number]]|The current block that the system is on|[[Block Number Type]]|||
|[[Global State-Block Difficulty\|Block Difficulty]]|The latest difficulty for blocks|[[Block Difficulty Type]]|||
|[[Global State-Current Hash Difference\|Current Hash Difference]]||[[Hash Type]]|||
|[[Global State-Historical Converted Qi\|Historical Converted Qi]]|An array of the conversions from Qi to Quai. The Qi Values will be negative in each entry and Quai values will be positive. Time is also logged in the entries of the array.|[[Conversions Array Type]]|||
|[[Global State-Historical Converted Quai\|Historical Converted Quai]]|An array of the conversions from Quai to Qi. The Quai Values will be negative in each entry and Qi values will be positive. Time is also logged in the entries of the array.|[[Conversions Array Type]]|||
|[[Global State-Historical Mined Ratio\|Historical Mined Ratio]]|An array of the historical ratios of mining between Qi and Quai which the miners had chosen at given times.|[[Mined Ratio Array Type]]|||
|[[Global State-Historical Qi Hash\|Historical Qi Hash]]|An array of the historical amount of hash attributed to Qi in block rewards with block numbers attatched to each entry.|[[Hash Array Type]]|||
|[[Global State-Historical Quai Hash\|Historical Quai Hash]]|An array of the historical amount of hash attributed to Quai in block rewards with block numbers attatched to each entry.|[[Hash Array Type]]|||
|[[Global State-K Qi\|K Qi]]|The controller coeffecient for Qi.|[[Coeffecient Type]]|||
|[[Global State-K Quai\|K Quai]]|The controller coeffecient for Quai.|[[Coeffecient Type]]|||
|[[Global State-Quai Price\|Quai Price]]|The current price of Quai.|[[USD Type]]|||
|[[Global State-Qi Price\|Qi Price]]|The current price of Qi.|[[USD Type]]|||
|[[Global State-Simulation History Log\|Simulation History Log]]|The logged data from simulation history.|[[Simulation History Log Type]]|||


## Boundary Actions
## Mechanisms Impacting the Entity
### [[Increment Block Number Mechanism]]
### [[Update Historical Mined Ratio Mechanism]]
### [[Update Historical Qi Hash Mechanism]]
### [[Update Historical Quai Hash Mechanism]]
### [[Mint Qi Tokens Mechanism]]
### [[Mint Quai Tokens Mechanism]]
## Actions Impacting the Entity
### [[Mine Block Boundary Action]]