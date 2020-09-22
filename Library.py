class Library:
	def __init__(self,list,name):
		self.booklist=list
		self.name=name
		self.lendDict={}

	def lendbooks(self):
		if self.lendDict=={}:
			print("no one took any book...")
		else:
			print("this is the lendbooks list which is already taken by some users..")
			for list in self.lendDict.items():
				print(list)


	def displayBooks(self):
		print(f"we have follwing books in Library:{self.name}")
		for book in self.booklist:
			print(book)

	def lendBook(self,user,book):
		if book not in self.lendDict.keys():
			self.lendDict.update({book:user})
			print("book has been updated,you can take now")
		else:
			print(f"book is already being used by  :{self.lendDict[book]}")


	def addBook(self,book):
		self.booklist.append(book)
		print("book has been added to the book list")

	def returnBook(self,book):
		if  book in self.lendDict:
			print("book has been successfully return..")
			self.lendDict.pop(book)
		else:
			print("the book you want to return is not from our Library...")

if __name__ == '__main__':
	harry=Library(["python","java","c","php"],"all in one")
	while (True):
		print(f"Welcome to the {harry.name}Library.Enter your choice ")
		print("1:Display books")
		print("2:Lend a book")
		print("3:Add a book")
		print("4:Return a book")
		choice=int(input())
		if choice==1:
			harry.displayBooks()
		elif choice==2:
			harry.lendbooks()
			book=input("Enter book name which you want to land")
			user=input("Enter Your name")
			harry.lendBook(user,book)
		elif choice==3:
			book=input("Enter book name which you want to add")
			harry.addBook(book)
			
		elif choice==4:
			book=input("Enter book name which you want to return..")
			harry.returnBook(book)
		else:
			print("Invalid choice")


		print("press q to quit and c to continue")
		user_choice2=''
		while (user_choice2!="c" and user_choice2!="q"):
			user_choice2=input()
			if user_choice2=="q":
				exit()
			elif user_choice2=="c":
				continue



