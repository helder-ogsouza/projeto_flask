from abc import ABC, abstractmethod

class SensorTemperatura(ABC):
    @abstractmethod
    def ler(self) -> str:
        pass

class ModuloIrrigacao(ABC):
    @abstractmethod
    def acionar(self) -> str:
        pass

class FabricaAgricultura(ABC):
    @abstractmethod
    def criar_sensor_temperatura(self) -> SensorTemperatura:
        pass

    @abstractmethod
    def criar_modulo_irrigacao(self) -> ModuloIrrigacao:
        pass
