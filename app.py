#!/usr/bin/python
from Vista.vistaLab import VistaLab

ver = VistaLab()
try:
    ver.main_loop()
except KeyboardInterrupt:
    print("\nEjecucion de GOLAB Interrumpida.")#combinacion ctrl c
except EOFError:
    print("\nEjecucion Interrumpida de GOLAB ")#combinacion ctrl d
except Exception:
    print("\nError consulte con su proveedor de servicios ")

