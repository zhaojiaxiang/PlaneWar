from PlaneWar.game.war import PlaneWar


def main():
    """ 飞机大战入口函数 """
    war = PlaneWar()
    war.add_small_enemies(6)
    war.run_game()


if __name__ == "__main__":
    main()