from PlaneWar import constants


class PlayResult():
    """玩家的结果统计"""
    __score = 0     # 总分
    __life = 3      # 生命数量
    __blood = 1000  # 生命值

    @property
    def score(self):
        """单次游戏分数"""
        return self.__score

    @score.setter
    def score(self, value):
        if value < 0:
            return None
        self.__score = value

    def set_history(self):
        """记录最高分"""
        # 读取文件中存储的分数
        # 存储分数不是追加，而是替换
        if int(self.get_max_score()) < self.score:
            with open(constants.PLAY_RESULT_STORE_FILE, 'w') as f:
                f.write('{}'.format(self.score))

    def get_max_score(self):
        """读取文件中的历史最高分"""
        rest = 0
        with open(constants.PLAY_RESULT_STORE_FILE, 'r') as f:
            r = f.read()
        if r:
            rest = r
        return rest
