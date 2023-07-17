import logging

logging.getLogger().setLevel(logging.INFO)

while True:
    try:
        numb = int(input("Введи всій вік: "))
    except ValueError as e:
        logging.ERROR
        logging.error(e)
        logging.info("Треба вводити тіко цифри")
    else:
        break

print(f"Your age is {numb}")