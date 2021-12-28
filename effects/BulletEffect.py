from abc import ABC, abstractmethod


class BulletEffect(ABC):

    duration: float
    applied_at: float | None = None
    is_already_applied: bool = False

    @abstractmethod
    def apply_effect(self, enemy):
        raise NotImplementedError()

    @abstractmethod
    def on_effect_expired(self, enemy):
        pass
