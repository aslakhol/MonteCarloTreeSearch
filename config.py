nim = dict(pieces=11, max_take=3)

ledge = dict(initial_board="000002000")

general = dict(
    verbose=True,
    win_statistics_batch=True,
    game="ledge",
    starting_player="one",  # one, two or mix
    episodes=50,
    M=10000,
    c=1,
)
