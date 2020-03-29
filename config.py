nim = dict(pieces=11, max_take=3)

ledge = dict(initial_board="1001020010")

general = dict(
    verbose=True,
    win_statistics_batch=True,
    game="ledge",
    starting_player="one",  # one, two or mix
    episodes=50,
    M=500,
    c=2,
)
