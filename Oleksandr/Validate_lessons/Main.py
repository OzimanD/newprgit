from Objects import *
from Methods import *

print_workers(employees)
print("Кількість працівників старших за 60 років:",count_workers_older_60(employees))
write_file(employees)
read_file()