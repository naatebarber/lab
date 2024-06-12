import time


def stutter_forever(word):
    stutter_up = True
    stutter_index = 0

    # Do whatever is in while True repeatedly, forever
    while True:
        print(word[0 : stutter_index + 1])

        if stutter_up:
            stutter_index += 1
        else:
            stutter_index -= 1

        if stutter_index == 0:
            stutter_up = True
            continue

        if stutter_index == len(word) - 1:
            stutter_up = False
            continue

        time.sleep(0.1)


word_to_stutter = "pancake"

stutter_forever(word_to_stutter)
