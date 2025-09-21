import sys
import requests

for module_name, module_pass in sys.modules.items():
    print(module_name, module_pass)
    print("--------------------------")
