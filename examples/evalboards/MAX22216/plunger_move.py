import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import MAX22216
from pytrinamic.evalboards import MAX22216_eval
import time

pytrinamic.show_info()

with ConnectionManager(debug=True).connect() as my_interface:
    print(my_interface)

    eval = MAX22216_eval(my_interface)
    ic = eval.ics[0]
    solenoid = ic.motors[0]

    solenoid.u_supply = 24.0 # V
    solenoid.u_dc_h = 24.0 # V
    solenoid.u_dc_l = 0.0 # V
    solenoid.u_dc_l2h = 24.0 # V 
    solenoid.u_dc_h2l = 0.0 # V
    solenoid.u_ac = 1.0 # V ampl
    solenoid.f_ac = 50.0 # Hz

    solenoid.set_high()
    time.sleep(1.0)
    solenoid.set_low()
    time.sleep(1.0)
    

print("\nDone.")