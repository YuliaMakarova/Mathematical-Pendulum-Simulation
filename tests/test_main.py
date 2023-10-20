import sys
import os
import unittest
import numpy as np
from scipy.integrate import odeint

# Получаем путь к текущему каталогу скрипта
current_dir = os.path.dirname(os.path.abspath(__file__))
# Добавляем путь к родительскому каталогу
sys.path.append(os.path.join(current_dir, '..'))
from main import pendulum


class TestPendulumSimulation(unittest.TestCase):
    def test_theta_length(self):
        """
        Тест проверяет соответствие длины массива `theta` длине массива `t`.

        Математический маятник моделируется с использованием дифференциальных уравнений.
        В этом тесте мы проверяем, что длина массива углов `theta`, полученных при решении
        уравнений, соответствует длине массива временных интервалов `t`.

        Тест использует заданные значения длины `L`, начального угла `initial_angle`,
        угловой скорости `omega0` и ускорения свободного падения `g` для моделирования маятника.

        Returns:
            None
        """
        L = 1
        initial_angle = 45

        # Преобразование начального угла в радианы
        theta0 = np.deg2rad(initial_angle)
        omega0 = 0.0

        g = 9.81  # ускорение свободного падения (м/с^2)

        # Временной интервал
        t = np.linspace(0, 10, 1000)

        # Решаем дифференциальное уравнение для моделирования маятника
        y = odeint(pendulum, [theta0, omega0], t, args=(L, g))
        theta = y[:, 0]

        # Проверяем, что длина массива `theta` соответствует длине массива `t`
        self.assertEqual(len(theta), len(t))


if __name__ == '__main__':
    unittest.main()
