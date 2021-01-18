from abc import ABCMeta, abstractclassmethod
# 引入ABCMeta, abstractclassmethod定义抽象类和抽象方法
# 监听模式


class Observer(metaclass=ABCMeta):
    """观察者的基类"""

    @abstractclassmethod
    def update(self, observable, object):
        pass


class Observable:
    """
    被观察者的基类
    """

    def __init__(self) -> None:
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        for o in self.__observers:
            o.update(self, object)

# 例子，热水器使用


class WaterHeater(Observable):
    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("当前温度是："+str(self.__temperature), "`C")
        self.notifyObservers()


class WashingMode(Observer):
    """
    该模式用于洗澡
    """

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 50 and observable.getTemperature() <= 70:
            print("水已经烧好！温度正好：可以用过来洗澡了")


class DrinkingMode(Observer):
    """
    该模式用于饮水
    """

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("水已经烧好！可以用过来饮用了")


if __name__ == "__main__":
    heater = WaterHeater()
    heater.addObserver(WashingMode())
    heater.addObserver(DrinkingMode())
    heater.setTemperature(40)
    heater.setTemperature(70)
    heater.setTemperature(100)
