from person import Person
import logging

logging.basicConfig(filename='sub.log', filemode='a', level=logging.INFO)


def sub(a, b):
    if b != 0:
        return a / b
    elif b == 0:
        logging.debug(f"a/b= {str(a)}/{str(b)}")
        logging.info("Divide by zero!")


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)

# logging debug nabayad dakhele halqe bashe. chon ya qablesh return mishe tabe va be in nemirese ya aslan dakhelesh
# nemire. hatta agar yek tab ham aqab biad baz qalate chon addad taqsim bar 0 ro mikhad namayesh bede.
# nokteye bad ham levele debug va info hast.
############################################################################

