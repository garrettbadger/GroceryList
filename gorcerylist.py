
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("C:\\Users\\Garrett\\Downloads\\grocerylist-36cb8-9d2e01e302fd.json")
firebase_admin.initialize_app(cred)

db=firestore.client()
add = 0
# Add Data
def start_list(add):
	#This function serves to create a template for the database. If you have an empty data base then you can set the add variable to 1 and create a template from which to start the program.
	if add == 1:
		db.collection("Grocery_List").document("Walmart").set({'Cinnamon Toast Crunch': 2, 'Granola Bars': 1, 'Ice Cream': 1, 'Crackers': 1})
		db.collection("Grocery_List").document("Costco").set({'Milk': 2, 'Chicken Breast': 1, 'Eggs': 60})
		db.collection("Grocery_List").document("Broulims").set({'Apples': 6, 'Oranges': 3, 'Bananas': 10})
	else:
		return
	
start_list(add)	



class Grocery_list():
	def __init__(self) -> None:
		pass

	def read_data(self, document):
		#This method serves to read the data from whichever document was selected by the user within the database
		doc = db.collection('Grocery_List').document(document).get()
	
		print(f'\n{doc.to_dict()}\n')
		pass

	def update_data(self, document, field, increment):
		#This method will update an existing field in the database. You can increase or decrease the amount of that item that you need.
		db.collection('Grocery_List').document(document).update({field:increment})
		pass

	def delete_data(self, document, field):
		#This method serves to delete a specific field in the database. If you got all of the item you needed off your list you can delete it here.
		db.collection('Grocery_List').document(document).update({field:firestore.DELETE_FIELD})
		pass

	def add_data(self, document, data):
		# This method will add a new field with a value for the quantity of that item that you need.
		db.collection('Grocery_List').document(document).set(data, merge=True)
		pass


def main():
	shopping = True
	gList = Grocery_list() #create a class object
	print("\nWelcome to your personalized Grocery List tool!\n")
	store = input("\nWhich store are you at right now? (W: Walmart, C: Costco, B: Broulims)\n")
	#Based on what the user inputs it will select the appropriate list for the corresponding store
	if store == 'W':
		store = 'Walmart'
		gList.read_data(store)
	elif store == 'C':
		store = 'Costco'
		gList.read_data(store)
	elif store == 'B':
		store = 'Broulims'
		gList.read_data(store)
	else:
		print('\nPlease input either W, B, or C for the corresponding store you are at.\n')
	while shopping:
		#Gives the user the option to either Add, Delete, or Update an item
		choice = input('\nWhat would you like to do? (A: add item, U: update item, D: delete item)\n')
		if choice == 'A':
			item = input('\nWhat would you like to add to your list?\n') #specify what you would like to add
			quantity = input(f'\nHow many {item}(s) do you want?\n') #specify how much of said item you want
			data = {item.replace(" ", ''): int(quantity)} #set the data into a format that the database recognizes
			gList.add_data(store, data) #add the data to the database
			gList.read_data(store) #print out the new data for the user to see
		elif choice == 'U':
			item = input('\nWhat item would you like to update?\n') #select which item to update
			quantity = input(f'\nYou can choose to update the quantity of the item needed. How many {item}(s) do you need?\n') #select the new amount of item needed
			gList.update_data(store, item.replace(" ", ""), int(quantity)) #replace the existing data
			gList.read_data(store) #display updated data for user to see
		elif choice == 'D':
			item = input("\nWhich item would you like to remove from your list?\n") #select which item to delete
			gList.delete_data(store, item.replace(" ", "")) #delete the specified item
			gList.read_data(store) #display update information for the user to see
		else:
			print("\nPlease input either A, U, or D depending on what you would like to do.\n")
		still_shopping = input('\nAre you still shopping? (yes or no)\n') #check if user is still shopping
		if still_shopping == 'yes':
			shopping = True
		elif still_shopping == 'no':
			shopping = False #if they are not shopping anymore than the loop will exit and the program will close
		else:
			print("\nplease input yes or no.\n")
		if shopping == False:
			print("\nThank you for using our shopping tool today!\n")

	
if __name__ == "__main__":
    main()

