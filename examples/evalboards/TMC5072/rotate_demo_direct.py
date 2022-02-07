"""
Move a motor back and forth using velocity and position mode of the TMC5072
"""
import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5072_eval

pytrinamic.show_info()
myInterface = ConnectionManager().connect()
print(myInterface)

eval_board = TMC5072_eval(myInterface)
ic = eval_board.ics[0]

print("Preparing parameters")
ic.MOTORS[0].write_axis_field(ic.FIELDS.A1, 1000)
ic.MOTORS[0].write_axis_field(ic.FIELDS.V1, 50000)
ic.MOTORS[0].write_axis_field(ic.FIELDS.D1, 500)
ic.MOTORS[0].write_axis_field(ic.FIELDS.DMAX, 500)
ic.MOTORS[0].write_axis_field(ic.FIELDS.VSTART, 0)
ic.MOTORS[0].write_axis_field(ic.FIELDS.VSTOP, 10)
ic.MOTORS[0].write_axis_field(ic.FIELDS.AMAX, 1000)
ic.MOTORS[1].write_axis_field(ic.FIELDS.A1, 1000)
ic.MOTORS[1].write_axis_field(ic.FIELDS.V1, 50000)
ic.MOTORS[1].write_axis_field(ic.FIELDS.D1, 500)
ic.MOTORS[1].write_axis_field(ic.FIELDS.DMAX, 500)
ic.MOTORS[1].write_axis_field(ic.FIELDS.VSTART, 0)
ic.MOTORS[1].write_axis_field(ic.FIELDS.VSTOP, 10)
ic.MOTORS[1].write_axis_field(ic.FIELDS.AMAX, 1000)

print("Rotating motor 1")
ic.MOTORS[0].rotate(10*25600)

time.sleep(5)

print("Stopping motor 1")
ic.MOTORS[0].stop()

time.sleep(1)

print("Rotating motor 2")
ic.MOTORS[1].rotate(10*25600)

time.sleep(5)

print("Stopping motor 2")
ic.MOTORS[1].stop()

time.sleep(1)

print("Moving back to 0")
ic.MOTORS[0].move_to(0, 100000)

# Wait until position 0 is reached
while eval.MOTORS[0].actual_position != 0:
    pass

print("Reached Position 0")

myInterface.close()
