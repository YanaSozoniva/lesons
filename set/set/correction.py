def get_circle_area(r: float) -> float:
    """находит площадь окружности"""
    pi = 3.14
    circle_area = pi * r**2
    return circle_area


def format_description(r: float, area: float) -> str:
    """Форматированный вывод информации об окружности"""
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))


def get_circle_info(r: float) -> None:
    """получение информации об окружности"""
    area = get_circle_area(r)
    description = format_description(r, area)
    print(description)


radius = int(input("Enter circle radius (int): "))
get_circle_info(radius)
