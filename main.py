from demoparser2 import DemoParser

parser = DemoParser("./replays/wingman.dem")
event_df = parser.parse_event("player_death", player=["X", "Y"], other=["total_rounds_played"])
ticks_df = parser.parse_ticks(["X", "Y"])

print(ticks_df)
