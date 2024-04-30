# Call of Duty Warzone "Ranked Play" Map Rotation
This is just a simple code to replicate the way the map in Call of Duty Warzone rotates with time.

If you're not familiar with Warzone ranked play, here's what happens:
players start the game in a relatively big map, they loot and kill each other (in the game of course) and as time passes, the map get smaller and smaller. Basically a deadly "gas" starts spreading, which limits the area that players can play in. The safe zone is always a circle, that starts big, containing the entire map, and gradually it gets smaller and smaller. The circle will be centered somewhere random in the map, stay there for a while, then the center will be moved somewhere else, alerting the players, and the safe zone slowly moves to the new location. This continues until radius of the circle is zero, or last team wins.

Here, I'm gonna imlement the whole circle shenanigan. Not a complex code, just something fun to do.
