import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules import TMCC160
import time

PyTrinamic.show_info()

# please select your CAN adapter
# myInterface = ConnectionManager("--interface pcan_tmcl").connect()
myInterface = ConnectionManager("--interface kvaser_tmcl").connect()

with myInterface:
    module = TMCC160(myInterface)
    motor = module.motors[0]

    # Define motor configuration for the TMCC160-EVAL.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # drive configuration
    motor.drive_settings.poles = 8
    motor.drive_settings.max_current = 2000
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_FOC_HALL
    motor.drive_settings.target_reached_velocity = 500
    motor.drive_settings.target_reached_distance = 5
    motor.drive_settings.motor_halted_velocity = 5
    print(motor.drive_settings)

    # hall sensor configuration
    motor.digital_hall.polarity = 0
    motor.digital_hall.interpolation = 0
    print(motor.digital_hall)

    # motion settings
    motor.linear_ramp.max_velocity = 4000
    motor.linear_ramp.max_acceleration = 2000
    motor.linear_ramp.enabled = 1
    print(motor.linear_ramp)

    # PI configuration
    motor.pid.torque_p = 600
    motor.pid.torque_i = 600
    motor.pid.velocity_p = 800
    motor.pid.velocity_i = 500
    motor.pid.position_p = 300
    print(motor.pid)

    time.sleep(1.0)

    # clear actual position
    motor.actual_position = 0

    print("\nRotate motor in clockwise direction...")
    motor.rotate(500)

    print("Press 'input_0' to swap the direction (waiting for input_0)\n")

    # wait for input_0
    while module.get_digital_input(module.DI.REF_R) == 1:
        print("actual position: %d   actual velocity: %d   actual torque: %d" % (motor.actual_position,
              motor.actual_velocity, motor.get_axis_parameter(motor.AP.ActualTorque, True)))
        time.sleep(0.2)

    print("\nRotate motor in counterclockwise direction...")
    motor.rotate(-500)

    print("Press 'input_1' to stop the motor (waiting for input_1)\n")

    # wait for input_1
    while module.get_digital_input(module.DI.REF_L) == 1:
        print("actual position: %d   actual velocity: %d   actual torque: %d" % (motor.actual_position,
              motor.actual_velocity, motor.get_axis_parameter(motor.AP.ActualTorque, True)))
        time.sleep(0.2)

    # stop motor
    motor.rotate(0)

print("\nReady.")
