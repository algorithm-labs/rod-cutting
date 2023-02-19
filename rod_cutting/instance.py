from typing import List

from pydantic import (
    BaseModel,
    confloat,
    conint,
)


class RodCuttingInstance(BaseModel):
    prices: List[confloat(ge=0.0)]     

    @property
    def p(self):
        return self.prices

    @property
    def rod_length(self):
        return len(self.prices)

    @property
    def n(self):
        return self.rod_length

    def restrict_to_rod_size(self, size: conint(ge=0.0)):
        return RodCuttingInstance(prices=self.prices[:size])

    def restrict(self, size: conint(ge=0.0)):
        return self.restrict_to_rod_size(size)