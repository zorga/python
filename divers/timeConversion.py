#!/usr/bin/python

def main():
    in_clock = raw_input().strip()
    morning = False
    if in_clock.endswith('AM'):
        morning = True

    hour = in_clock[0:2]
    minutes = in_clock[3:5]
    seconds = in_clock[6:8]

    if hour == '12' and morning:
        hour = '00'

    elif hour == '12' and not morning:
        hour = '12'
    
    elif not morning:
        hour = str(int(hour) + 12)

    res = hour + ':' + in_clock[3:5] + ':' + in_clock[6:8]
    print res

if __name__ == '__main__':
    main()
