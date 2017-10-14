import psycopg2

class House:

    def __init__(self, address):
        self.address = address
        self.balance = 0
        self.conn = psycopg2.connect("dbname='hm' user='postgres' password='p123' host='localhost' port='5432'")
        self.cur = self.conn.cursor()

    def insert_new_apartment(self, ap):

        self.cur.execute("INSERT INTO public.\"Apartments\" VALUES (%s,%s,%s,%s,%s,%s,%s)",
                        (ap.number, ap.owner, ap.owner_phone, ap.renter, ap.renter_phone, ap.month_payment, ap.square))
        self.conn.commit()

    def view_apartments_numbers(self):
        self.cur.execute("SELECT number FROM public.\"Apartments\"")
        rows = self.cur.fetchall()
        return rows

    def view_all_apartments(self):
        self.cur.execute("SELECT * FROM public.\"Apartments\"")
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()

class Apartment:

    def __init__(self, number):
        self.number = number

    owner = ""
    owner_phone = ""
    renter = ""
    renter_phone = ""
    month_payment = 0
    square = 0

class Person:

    def __init__(self, FirstName):
        self.FirstName = FirstName
        self.LastName = ""
        self.phone = ""

class Owner(Person):
    pass

class Renter(Person):
    pass


myHouse = House("17 Yosef Eliahu, Tel Aviv")

# ap1 = Apartment(2)
# ap1.owner = "Liza Cudrow"
# ap1.owner_phone = "052-3453456"
# ap1.month_payment = 120
#
# myHouse.insert_new_apartment(ap1)

for row in myHouse.view_all_apartments():
    print(row)
