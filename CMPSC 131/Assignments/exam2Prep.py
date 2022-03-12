def freqCalc(speedSound, velocityReceiver, velocitySource, freqSource):
    freqHeard = round(((speedSound+velocityReceiver)/(speedSound+velocitySource))*freqSource, 4)
    return freqHeard

def main():
    speedSound = 343
    velocityReceiver = int(input("Input the velocity of the receiver (m/s): "))
    velocitySource = int(input("Input the velocity of the source (m/s): "))
    freqSource = int(input("Input the frequency of the source (Hz): "))
    freqHeard = freqCalc(speedSound, velocityReceiver, velocitySource, freqSource)
    print("Heard frequency =",freqHeard,"Hz")

main()