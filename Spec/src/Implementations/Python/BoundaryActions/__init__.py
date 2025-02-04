from .Dummy import v1_dummy_boundary, v1_dummy_boundary2, v2_dummy_boundary2
from .Block import (
    mine_block_boundary_action_v1,
    mine_block_boundary_action_v2,
    test_mine_block_boundary_action,
    mine_block_boundary_action_v3,
    do_not_use_print_hello,
)
from .Conversions import (
    test_quai_conversion,
    test_qi_conversion,
    conversions_boundary_action_v1,
    do_not_use_conversion,
)
from .Market import test_price_movements_boundary, hashpower_price_movement
from .User import update_population_beta_boundary_action_signal

boundary_action_options = {
    "V1 Dummy Boundary Action Option": v1_dummy_boundary,
    "V1 Dummy Boundary Action 2 Option": v1_dummy_boundary2,
    "V2 Dummy Boundary Action 2 Option": v2_dummy_boundary2,
    "Mine Block Boundary Action V1": mine_block_boundary_action_v1,
    "TEST Quai Conversion": test_quai_conversion,
    "TEST Qi Conversion": test_qi_conversion,
    "TEST Price Movements Boundary": test_price_movements_boundary,
    "Mine Block Boundary Action V2": mine_block_boundary_action_v2,
    "Hashpower Price Movement": hashpower_price_movement,
    "Conversions Boundary Action V1": conversions_boundary_action_v1,
    "TEST Mine Block Boundary Action": test_mine_block_boundary_action,
    "Mine Block Boundary Action V3": mine_block_boundary_action_v3,
    "Update Population Beta Boundary Action Signal": update_population_beta_boundary_action_signal,
    "DO NOT USE Conversion": do_not_use_conversion,
    "DO NOT USE Print Hello Boundary Action V1": do_not_use_print_hello,
}
