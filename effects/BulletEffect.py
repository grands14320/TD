from abc import ABC, abstractmethod


class BulletEffect(ABC):
    """
    Defines an abstract class. Contains method that should be overridden
    """

    duration: float
    applied_at: float | None = None
    is_already_applied: bool = False

    @abstractmethod
    def apply_effect(self, enemy):
        """
        Should contain logic which will be executed when the bullet hits the enemy
        """
        raise NotImplementedError()

    @abstractmethod
    def on_effect_expired(self, enemy):
        """
        Should contain logic which will be executed when the bullet effect expires.
        """
        pass
