class Rapper():
	def __init__(self, rap_name, name, age, alias1, alias2, specialability):
		self.name = name
		self.rap_name = rap_name
		self.age = age
		self.alias1 = alias1
		self.alias2 = alias2
		self.specialability = specialability


outfile = open("RapperFactsDatabase.dat", "w")


#loop start
for rapstar in range(8):



        rap_name = input ("What is name ")
        #for use in f format in name variable prompt.
        name_string = rap_name


        name = input (f"What is {name_string}'s Birth Name")
        age = input (f"What is {name_string}'s age  ")
        alias1 = input(f"what is  {name_string}'s first alias ")
        alias2 = input (f"what is {name_string}'s second alias ")
        specialability = input (f"{name_string}'s Special move ")

        lyricist = Rapper(name, rap_name, age, alias1, alias2, specialability)
        print(lyricist.name + ",", lyricist.rap_name + ",", lyricist.age + ",", lyricist.alias1 + ",", lyricist.alias2 + ",", lyricist.specialability + ",")
        j =(lyricist.name, lyricist.rap_name, lyricist.age, lyricist.alias1, lyricist.alias2, lyricist.specialability)
        outfile.write(str(j)+"\n")

outfile.close()



