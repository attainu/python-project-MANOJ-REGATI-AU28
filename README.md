Parking Lot
Design a parking lot using Python

Setup

To run the program :

NOTE- the program is case sensitive

you can choose two ways to run from 1- MANUAL 2- FILE:

MANUAL - you have to provide information manually what u need to do i.e. create, park, leave etc.

FILE - you just need to select the file you need to run for eg:

type - S:\ashish-sharma-au-16\input\input_instruction.txt

FLAKE-8 - i have used flake8 to check mistakes and it shows NONE. (only for file name it shows)

Parking.py script defines the following functions

CreateParkinLot N - Given N number of slots to create a parking lot

park regdno colour - Parks a vehicle with given registration number and color in the empty slot . If there are no more empty slots available, it display a message "Parking lot is full".

status - Prints the slot number, registration number and color of the parked vehicles. leave N - Removes vehicle from slot number N Running the app

To run the app, just open the parking.py file on a console like Command Prompt.

Instructions and commands used by the program are as follows:

To create a parking lot, "CreateParkinLot " example : CreateParkingLot 6 [where 6 is number of slots]

To park a vehicle, "park " example : park KA white [where KA is the registration no and white is the color of car]

INPUT: -

CreateParkingLot 6

park KA-01-HH-1234 White

park KA-01-HH-9999 White

park KA-01-BB-0001 Black

park KA-01-HH-7777 Red

park KA-01-HH-2701 Blue

park KA-01-HH-3141 Black

leave 4

status

park KA-01-P-333 White

park DL-12-AA-9999 White

registration_numbers_for_cars_with_colour White

slot_numbers_for_cars_with_colour White

slot_number_for_registration_number

KA-01-HH-3141

slot_number_for_registration_number

MH-04-AY-1111

OUTPUT:-

Created a parking lot with 6 slots

Allocated slot number: 1

Allocated slot number: 2

Allocated slot number: 3

Allocated slot number: 4

Allocated slot number: 5

Allocated slot number: 6

Slot no 4 is free

Slot No. Registration No Colour

1 KA-01-HH-1234 White

2 KA-01-HH-9999 White

3 KA-01-BB-0001 Black

5 KA-01-HH-2701 Blue

6 KA-01-HH-3141 Black

Allocated slot number: 4

Parking lot is full, Sorry For Inconvinience

KA-01-HH-1234,KA-01-HH-9999,KA-01-P-333

not found

not found

not found

1,2,4

6

Not Found