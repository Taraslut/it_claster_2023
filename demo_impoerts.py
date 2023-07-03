from pkg1 import show_info
from pkg2 import rise_square

size = int(input("Enter rectangle size > "))

area = rise_square(size)

show_info("For rectangle size ", size=size)
show_info("We get ", area=area)
