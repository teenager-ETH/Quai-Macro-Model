from .Dummy import dummy_log_results_mechanism
from .MonetaryPolicy import (
    mint_qi_tokens_mechanism,
    mint_quai_token_mechanism,
    burn_qi_tokens_mechanism,
    burn_quai_tokens_mechanism,
    update_prices_mechanism,
    update_locked_qi_mechanism,
    update_locked_quai_mechanism,
)
from .Logs import (
    update_historical_converted_qi_mechanism,
    update_historical_converted_quai_mechanism,
)
from .Vesting import unlock_tokens_mechanism
from .Block import (
    update_block_difficulty_mechanism,
    append_to_unlock_schedule_mechanism,
)

mechanisms = {
    "DUMMY Log Results Mechanism": dummy_log_results_mechanism,
    "Mint Qi Tokens Mechanism": mint_qi_tokens_mechanism,
    "Mint Quai Tokens Mechanism": mint_quai_token_mechanism,
    "Burn Qi Tokens Mechanism": burn_qi_tokens_mechanism,
    "Burn Quai Tokens Mechanism": burn_quai_tokens_mechanism,
    "Update Historical Converted Qi Mechanism": update_historical_converted_qi_mechanism,
    "Update Historical Converted Quai Mechanism": update_historical_converted_quai_mechanism,
    "Update Prices Mechanism": update_prices_mechanism,
    "Unlock Tokens Mechanism": unlock_tokens_mechanism,
    "Update Block Difficulty Mechanism": update_block_difficulty_mechanism,
    "Update Locked Qi Mechanism": update_locked_qi_mechanism,
    "Update Locked Quai Mechanism": update_locked_quai_mechanism,
    "Append to Unlock Schedule Mechanism": append_to_unlock_schedule_mechanism,
}
