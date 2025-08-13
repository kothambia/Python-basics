class npc:
    name = "jason"
    age = 18
    sex = "male"
    country = "india"
    clothe = "casual"
    profession = "gangster"
    def info(self):
        print(f"""
my name is {self.name} and i am a {self.sex}
i am {self.age} years old. i come from {self.country}
my profession is a {self.profession}.
(This character wears {self.clothe} clothes)        """)

d = npc()
# npc 1
a = npc()
a.name = "Tushar"
a.clothe = "old money"
# npc 2
b = npc()
b.name = "Aryan"
b.clothe = "spider man"
# npc 3
c = npc()
c.name = "Ellie"
c.age = 21
c.clothe = "survival"
c.sex = "female"
c.profession = "Kill zombies"
c.country = "USA"
d.info()
