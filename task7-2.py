from abc import ABC, abstractmethod

from typing import Any

class AbstractClothes(ABC):

    @property
    @abstractmethod
    def tissue_required(self):
        pass

    @property
    @abstractmethod
    def measuring(self):
        pass

    @abstractmethod
    def _calc_tissue_required(self):
        pass


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, name: str, measuring: Any):
        self.name = name
        self._measuring = measuring
        self._tissue_required = None

        self._clothes.append(self)

    def _calc_tissue_required(self):
        raise NotImplemented

    @property
    def tissue_required(self):

        if not self._tissue_required:
            self._calc_tissue_required()

        return self._tissue_required

    @property
    def measuring(self):

        return self._measuring

    @measuring.setter
    def measuring(self, measuring: Any):

        self._measuring = measuring
        self._tissue_required = None

    @property
    def total_tissue_required(self):
        return sum([item.tissue_required for item in self._clothes])


class Coat(Clothes):

    def _calc_tissue_required(self):
        self._tissue_required = round(self.measuring / 6.5 + 0.5, 2)

    @property
    def V(self):
        return self.measuring

    @V.setter
    def V(self, size: Any):
        self.measuring = size

    def __str__(self):
        return f"On coat {self.measuring} size " \
               f"required {self.tissue_required} sq.m of fabric"


class Suit(Clothes):

    def _calc_tissue_required(self):
        self._tissue_required = round(2 * self.measuring * 0.01 + 0.3, 2)

    @property
    def H(self):
        return self.measuring

    @H.setter
    def H(self, height: Any):
        self.measuring = height

    def __str__(self):
        return f"For tailoring a suit for height {self.measuring} cm. " \
               f"required {self.tissue_required} sq.m of fabric"



coat = Coat('Coat', 5)
print(coat)
suit = Suit('sport suit', 178)
print(suit)
print(f'Total area of fabric {coat.total_tissue_required} sq.m')

coat.V = 10
print(coat)
suit.H = 200
print(suit)
print(f'Total area of fabric {suit.total_tissue_required} sq.m')