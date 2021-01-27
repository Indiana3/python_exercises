##
# Display the noise related to a db sound level
#
JACKHAMMER = 130
GASLAWNMOWER = 106
ALARM_CLOCK = 70
QUIET_ROOM = 40

# Read the value in db
sound = float(input("Please, enter a sound level in db: "))

# Determine the corresponding noise
if sound == JACKHAMMER:
    print(sound, "db correspond to the noise of a jackhammer")
elif sound == GASLAWNMOWER:
    print(sound, "db correspond to the noise of a gaslawnmower")
elif sound == ALARM_CLOCK:
    print(sound, "db correspond to the noise of a alarm clock")
elif sound == QUIET_ROOM:
    print(sound, "db correspond to the noise of a quiet room")
elif sound > JACKHAMMER:
    print(sound, "db correspond to a louder noise than a jackhammer")
elif GASLAWNMOWER < sound < JACKHAMMER:
    print(sound, "db correspond to the noise between a gas lawnmower and a jackhammer")
elif ALARM_CLOCK < sound < GASLAWNMOWER:
    print(sound, "db correspond to the noise between an alarm clock and a gas lawnmower")
elif QUIET_ROOM < sound < ALARM_CLOCK:
    print(sound, "db correspond to the noise between a quiet room and an alarm clock")
else:
    print(sound, "db correspond to a lower noise than a quiet room")
