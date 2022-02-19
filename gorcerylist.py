from re import L
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("C:\\Users\\Garrett\\Downloads\\grocerylist-36cb8-9d2e01e302fd.json")
firebase_admin.initialize_app(cred)

db=firestore.client()
add = 0
# Add Data
def start_list(add):
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
		doc = db.collection('Grocery_List').document(document).get()
	
		print(f'\n{doc.to_dict()}\n')
		pass

	def update_data(self, document, field, increment):
		db.collection('Grocery_List').document(document).update({field:increment})
		pass

	def delete_data(self, document, field):
		db.collection('Grocery_List').document(document).update({field:firestore.DELETE_FIELD})
		pass

	def add_data(self, document, data):
		db.collection('Grocery_List').document(document).set(data, merge=True)
		pass


def main():
	shopping = True
	gList = Grocery_list()
	print("\nWelcome to your personalized Grocery List tool!\n")
	store = input("\nWhich store are you at right now? (W: Walmart, C: Costco, B: Broulims)\n")
	
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
		choice = input('\nWhat would you like to do? (A: add item, U: update item, D: delete item)\n')
		if choice == 'A':
			item = input('\nWhat would you like to add to your list?\n')
			quantity = input(f'\nHow many {item}(s) do you want?\n')
			data = {item.replace(" ", ''): int(quantity)}
			gList.add_data(store, data)
			gList.read_data(store)
		elif choice == 'U':
			item = input('\nWhat item would you like to update?\n')
			quantity = input(f'\nYou can choose to update the quantity of the item needed. How many {item}(s) do you need?\n')
			gList.update_data(store, item.replace(" ", ""), int(quantity))
			gList.read_data(store)
		elif choice == 'D':
			item = input("\nWhich item would you like to remove from your list?\n")
			gList.delete_data(store, item.replace(" ", ""))
			gList.read_data(store)
		else:
			print("\nPlease input either A, U, or D depending on what you would like to do.\n")
		still_shopping = input('\nAre you still shopping? (yes or no)\n')
		if still_shopping == 'yes':
			shopping = True
		elif still_shopping == 'no':
			shopping = False
		else:
			print("\nplease input yes or no.\n")
		if shopping == False:
			print("\nThank you for using our shopping tool today!\n")

	
if __name__ == "__main__":
    main()

