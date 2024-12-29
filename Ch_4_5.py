from datetime import datetime

# Function to format the current date
def format_date():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%A, %d %B %Y, %I:%M:%S %p")
    # %m gives you the month in numeric form, while %B gives you the month in full name form.
    print(f"Formatted Date: {formatted_date}")

# Function to calculate the difference in days between birthday and today
def days_until_birthday(birthday_str):
    """
    :param birthday_str: Birthday in 'YYYY-MM-DD' format.
    """
    # Convert birthday string to a datetime object
    birthday_date = datetime.strptime(birthday_str, "%Y-%m-%d")
    #strptime is a method from the datetime module. It stands for "string parse time" and is used to create a datetime object from a string, based on a specified format.
    today_date = datetime.now()

    # Adjust the year of the birthday to the current year
    birthday_date = birthday_date.replace(year=today_date.year)

    # If the birthday has already occurred this year, adjust to the next year
    if birthday_date < today_date:
        birthday_date = birthday_date.replace(year=today_date.year + 1)

    # Calculate the difference
    days_difference = (birthday_date - today_date).days
    print(f"Days until your next birthday: {days_difference} days")

# Format the current date
format_date()
# Input your birthday (in YYYY-MM-DD format)
birthday = input("Enter your birthday (YYYY-MM-DD): ")
days_until_birthday(birthday)

