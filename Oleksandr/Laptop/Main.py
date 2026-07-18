from Objects import *
from Methods import *


results = analyze_laptops(laptops)
write_file(results)
restored_results = read_file()
print_results(restored_results)