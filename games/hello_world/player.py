class Player:
    def __init__(self):
        self.ammo = 0
        self.armor = 10
        self.action = None

    def _add_ammo(self):
        self.ammo += 1
        print("reload")

    def _update_ammo_from_shot(self):
        assert self.ammo > 0
        self.ammo -= 1
        print("shot")
