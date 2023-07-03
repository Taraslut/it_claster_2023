from pkg1 import show_info, my_promt
from pkg2 import rise_square

size = my_promt()

area = rise_square(size)

show_info("For rectangle size ", size=size)
show_info("We get ", area=area)
