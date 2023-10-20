import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.integrate import odeint


def pendulum(y, t, L, g):
    """
    Решает дифференциальное уравнение для математического маятника.

    Parameters:
        y (list): Список, содержащий текущий угол и угловую скорость [theta, omega].
        t (float): Текущее время.
        L (float): Длина нити маятника.
        g (float): Ускорение свободного падения.

    Returns:
        list: Список с производными [dtheta/dt, domega/dt].
    """
    theta, omega = y
    dydt = [omega, -g / L * np.sin(theta)]
    return dydt


# Ввод длины нити и начального угла с консоли
L = float(input("Введите длину нити (м): "))
initial_angle = float(input("Введите начальный угол (градусы): "))

# Преобразование угла в радианы
theta0 = np.deg2rad(initial_angle)
omega0 = 0.0  # Начальная угловая скорость

# Ускорение свободного падения
g = 9.81  # м/с^2

# Временной интервал
t = np.linspace(0, 10, 1000)

# Решаем дифференциальное уравнение
y = odeint(pendulum, [theta0, omega0], t, args=(L, g))  # Массив y содержит углы и угловые скорости
theta = y[:, 0]  # Угол отклонения математического маятника от вертикали с течением времени

# Координаты шарика
x = L * np.sin(theta)
y = -L * np.cos(theta)

# Отображение движения маятника
fig, ax = plt.subplots()
ax.set_aspect('equal')

# Установка пределов координатных осей для области, в которой будет отображаться маятник
ax.set_xlim([-L, L])
ax.set_ylim([-L, 0])

# Создание объекта `line`, который будет представлять маятник в виде линии с точкой внизу
line, = ax.plot([], [], 'o-', lw=2)


def animate(i):
    """
    Функция для обновления анимации движения математического маятника.

    Параметры:
    i (int): Номер текущего кадра анимации.

    Возвращает:
    line (matplotlib.lines.Line2D): Объект, представляющий маятник в виде линии с точкой.

    Примечания:
    Функция обновляет положение маятника на основе текущего времени (i-й момент времени) и
    возвращает объект `line`, представляющий положение маятника для данного кадра анимации.
    """
    line.set_data([0, x[i]], [0, y[i]])
    return line,


# Создание анимации с использованием библиотеки `matplotlib.animation`
ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=20, blit=True)

# Установка заголовка для графика
ax.set_title('Движение математического маятника')

plt.show()