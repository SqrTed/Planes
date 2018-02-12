from controller.bigboss import Boss
from controller.controller import PlayerController
from domain.entities import Board
from ui.UI import UI

player_planes = Board()
player_hits = Board()
player = PlayerController(player_planes, player_hits)
computer_planes = Board()
computer_hits = Board()
computer = PlayerController(computer_planes, computer_hits)
controller = Boss(player, computer)
ui= UI(controller)
ui.run()
# player.new_plane(Point("E", 4, "W"))
# player.new_plane(Point("A", 3, "N"))


