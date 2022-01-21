import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules import TMCM1140
import time

PyTrinamic.show_info()

# for serial interface
# myInterface = ConnectionManager("--interface serial_tmcl --port COM6 --data-rate 115200").connect()

# for usb interface
myInterface = ConnectionManager().connect()

print(myInterface)

with myInterface:
    module = TMCM1140(myInterface)
    motor = module.motors[0]

    # The configuration is based on our PD42-1-1140-TMCL
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not working.

    print("Preparing parameters...")

    # preparing drive settings
    motor.drive_settings.max_current = 1000
    motor.drive_settings.standby_current = 0
    motor.drive_settings.boost_current = 0
    motor.drive_settings.microstep_resolution = motor.ENUM.MicrostepResolution256Microsteps
    print(motor.drive_settings)

    # preparing linear ramp settings
    motor.linear_ramp.max_acceleration = 1000
    motor.linear_ramp.max_velocity = 1000
    print(motor.linear_ramp)

    time.sleep(1.0)

    # clear position counter
    motor.actual_position = 0

    # start rotating motor for 5 sek
    print("Rotating...")
    motor.rotate(1000)
    time.sleep(5)

    # stop rotating motor
    print("Stopping...")
    motor.stop()

    # read actual position
    print("ActualPosition = {}".format(motor.actual_position))
    time.sleep(2)

    print("Doubling moved distance.")
    motor.move_by(motor.actual_position)

    # wait till position_reached
    while not motor.get_position_reached():
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)

    print("Furthest point reached.")
    print("ActualPosition = {}".format(motor.actual_position))

    # short delay and move back to start
    time.sleep(3)
    print("Moving back to 0...")
    motor.move_to(0)

    # wait until position 0 is reached
    while not motor.get_position_reached():
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)

    print("Reached position 0.")

print("\nReady.")
