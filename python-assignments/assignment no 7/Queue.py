'''
	Implementation of Queue
	Author:		Ranjit
	Date:		5/8/2017


'''
class Queue:
	def __init__(self):
		self.l=list()
		self.start=0;
	def insert(self,value):
		self.l.append(value)
		
	def remove(self):
		if self.start>len(self.l)-1:
			try:
				raise(ValueError())
					
			except ValueError as error:
				print "ValueError"		
		else:
			print(self.l.pop(self.start))
			


queue = Queue()
queue.insert(5)
queue.insert(6)
queue.remove()
queue.insert(7)
queue.remove()
queue.remove()
queue.remove()

	
		
