from person import Person
import logging

logging.basicConfig(level=logging.INFO)


# logging.FileHandler('sample.log', mode='a', encoding=None, delay=False)


def sub(a, b):
    logger = logging.getLogger('sample.py')
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler("sample.log")
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s-%(name)-10s-%(levelname)-16s-%(msecs)s-%(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    if b != 0:
        logging.debug("a/b=" + str(a / b))
        return a / b
    logging.info("Divide by zero!")


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)

###############################################################################################################
# avvalin moredi ke khode pycharm ham azamoon mikhad avaz konim esme class e person hast. dovvomin mored jaaye
# eshtebahe logging.debug hast ke bad az return oomade. bad az return dige chizi daakhele tabe ejra nmishe
###############################################################################################################
