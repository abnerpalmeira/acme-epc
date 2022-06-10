# ACME Employee Payment Calculator
<p align="center">

[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
</p>

## Usage

This program allows you to calculate how much an ACME employee will receive, given an input describing his working hours; The input may contain multiple employees; each one of them should follow the pattern below:

```
[NAME]=[DAY OF WEEK][STARTING HOUR]-[ENDING HOUR]
```
<b>[NAME]</b> = Name of the employee.\
<b>[DAY OF WEEK]</b> = Day of week it could be MO,TU,WE,TH,FR,SA,SU. \
<b>[STARTING HOUR]</b> = Time when the employee started working.\
<b>[ENDING HOUR]</b> = Time when the employee stoped working. \
When dealing with multiple employees, split it using comma.

Examples:
```
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ABNER=MO18:30-18:45
```

You can expected the following outputs:
```python
#Valid input.
The amount to pay ABNER is: 5.00 USD 

#Validation error
Line x of input is invalid.

#Validation error
Invalid input in Line {idx+1} the starting hour is greater than ending hour.
```
You can change the input by modifying the input.txt file.\
You can change the payment values and intervals by changing the data.json file.

## Run
Go to the project directory and run:

```bash
python3 main.py
```

## Approach and Methodology

When designing the solution, four factors caught my attention; the system would handle money; the format of a valid input is very specific; the hourly rate table should be stored in a place easy to change, and how to deal with incomplete working hours.

### Float precision
Because of the way floats are represented on the processor, they aren't a reliable data type to deal with money; check out the examples below:

```python
>>> 165 * 1.40
230.99999999999997

>>> 1.01 - 0.99
0.020000000000000018
```
With this in mind I decided to represent the amounts as integers multiplied by 100; this way I could keep the relevant decimal places for a financial application.

### Input Validation
In order to prevent the user from entering invalid data I decided to create a validation layer, but the input was very specific and to validate in a normal way I would end up with a very long code with several ifs, to solve this I created a regex expression that recognizes only inputs in the specified format.
```
^([a-zA-Z]+)=(((MO|WE|FR|T[HU]|S[AU])(0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9]-(0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9](,|$))+)$
```
### Hourly Rate Table
I needed to keep the rates  table in a place that was easy to change, to allow people without access to the code to change the rates. Since I didn't work with any database on this project, I decided to store it in a JSON file for its ease of manipulation and native compatibility with python.

### Incomplete Working Hours

Because there is the possibility of an employee getting paid for an hour that he didn't work fully, I decided to work with minutes instead of hours; this also made it much easier to check for interval overlapping. Working with minutes, the logic came down to three cases: the working interval is fully contained in a current rate interval, or it's partially contained, or it isn't contained at all.
It made the implementation easy because only two of these cases needed code.

### Conclusion
Besides the above facts the rest of my approach was pretty standard, I used classes, constants and tried to keep everything organized and simple. For styling I used black. 

## Tests
To to avoid the use of third party libraries I used unittest for testing.

## Future Improvements
- Accept different currencies.
- Enhance the testing class with pytest and fixtures.
- Dockerizing the application.

