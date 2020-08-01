# Use this playground to experiment with list methods, using Test Run
states = ["Lagos", "Oyo", "Ogun", "Osun", "Ondo", "Ekiti", "Kano", "Katsina", "Gombe", "Sokoto", "Kaduna", "Bauchi", "Yobe",
          "Adamawa", "Niger", "Jigawa", "Plateau", "Enugu", "Edo", "Ebonyi", "Rivers", "Nasarawa", "Anambra", "Abia", 
          "Cross River", "Akwa Ibom", "Bayelsa", "Benue", "Zamfara", "Borno", "Kebbi", "Fct", "Taraba", "Kogi",
          "Kwara", "Delta", "Imo"]

nigeria = states
print(nigeria)

print(len(nigeria))     #length of variable list
print(max(nigeria))     #great element in the list
print(min(nigeria))     #least element in the list

#rearrange the list 
print(sorted(nigeria))
print(sorted(nigeria, reverse=True))
nigeria = sorted(nigeria)
#replace states with there capital


#print(nigeria)     i hope this hasn't gone overboard. i came across this loop method while looking for a way to replace 
                    # a list variable without calling the index number
def find(data:list, val:object) -> object:
    counter = 0
    for x in sorted(data):
        counter=counter+1
        if( x == val):
            return counter

        

print(find(nigeria, 'Oyo'))

nigeria[find(nigeria, 'Oyo') -1] = "Ibadan"
print(nigeria)

   