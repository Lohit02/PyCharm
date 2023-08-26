from oops.multi3 import tree


class Animmal:
    def eat(self):
        print('The animal is eating')


class Rabbit(Animmal):
    def eat(self):
        print('Rabbit eat grass')

    pass


class Cocked(Animmal):
    pass


class Cock(tree):
    pass


ck = Cock()
ck.eat()
bk = Cocked()
bk.eat()

rabbit = Rabbit()
rabbit.eat()

cat = Animmal()
cat.eat()
