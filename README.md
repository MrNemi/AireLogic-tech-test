# Tech-Test
Patient Appointment Backend

# Task
Develop a CRUD application backend.
This project was developed using Flask for the API framework and SQlite for database management, with VSCode as the code editor.

## Running the API
1. First, install the virtual environment `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Activate the virtual environment using the command:
```
$ .\env\Scripts\activate  (for Windows)
```
```
$ source venv/bin/activate  (for Linux and MacOS)
```

4. Install the dependencies via requirements.txt:
```
$ (env) pip install -r requirements.txt
```

5. Finally, start the web server:
```
$ (env) python main.py
```

This server is coded to start on port 5000 by default. You can change this in `main.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(host='localhost', port = <desired port>, debug =True)
```

## Interacting with the API

Interacting with the API can be done either via the CLI of the code editor or directly on the web server once it is running. 
Any changes made to 'main.py' is immediately reflected on the server page as it automatically updates once the program is saved.

## Challenges

Most of the allotted project time was spent figuring out an optimal approach for developing the API. Given additional time, all key functionalities are certain to be implemented.

## Future Implementation
# I. Complete HTML files for editing patient and appointment details

# II. NHS number checksum validation
1. Create variable 'total'.

2. Iterate through first 9 digits of patient's NHS number, multiplying each one by the corresponding weighing factor (Tenth digit of patient's NHS number is assigned to 'check_digit' variable.).

3. Add up all products and assign result to the variable 'total' i.e.
```
    total = sum of all products
```

4. Variable 'remnant' = modulus(total/11)

5. new_check_digit = 11 - remnant

6. if (remnant == new_check_digit):
        'NHS number is valid'
    else:
        'NHS number is invalid'


## Notes

The author 'Orion9551' is my initial GitHub profile set up using my university email. This has recently been updated to match my current GitHub author credentials i.e. MrNemi.
