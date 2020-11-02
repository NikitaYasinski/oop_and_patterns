from abc import ABC, abstractmethod

class AbstractEffect(ABC, Hero):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass

class AbstractPositive(AbstractEffect):
    def get_negative_effects(self):
        return self.base.get_negative_effects()

class AbstractNegative(AbstractEffect):
    def get_positive_effects(self):
        return self.base.get_positive_effects()


class Berserk(AbstractPositive):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] += 7
        stats["Perception"] -= 3  # восприятие
        stats["Endurance"] += 7  # выносливость
        stats["Charisma"] -= 3  # харизма
        stats["Intelligence"] -= 3  # интеллект
        stats["Agility"] += 7  # ловкость
        stats["Luck"] += 7  # удача
        stats["HP"] += 50
        return stats

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Berserk"]


class Blessing(AbstractPositive):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] += 2
        stats["Perception"] += 2  # восприятие
        stats["Endurance"] += 2  # выносливость
        stats["Charisma"] += 2  # харизма
        stats["Intelligence"] += 2  # интеллект
        stats["Agility"] += 2  # ловкость
        stats["Luck"] += 2  # удача
        return stats

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Blessing"]


class Curse(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()

        stats["Strength"] -= 2
        stats["Endurance"] -= 2
        stats["Agility"] -= 2
        stats["Luck"] -= 2
        stats["Perception"] -= 2
        stats["Charisma"] -= 2
        stats["Intelligence"] -= 2
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ['Curse']


class Weakness(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()

        stats["Strength"] -= 4
        stats["Endurance"] -= 4
        stats["Agility"] -= 4
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ['Weakness']


class EvilEye(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Luck"] -= 10
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ['EvilEye']



