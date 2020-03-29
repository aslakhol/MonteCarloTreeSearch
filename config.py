nim = dict(pieces=11, starting_player=1, number_in_batch=100, max_take=3)

ledge = dict(
    number_in_batch=100,
    initial_board="1001020010",
    starting_player=1,
    number_of_simulations=12,
)

general = dict(
    verbose_mode=False,
    win_statistics_batch=True,
    game="ledge",
    starting_player="one",  # one, two or mix
    episodes=50,
    M=500,
    c=2,
)
