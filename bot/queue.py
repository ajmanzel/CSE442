class Queue:
   def __init__(self):
        self.front = 0
        self.SongQueue = []
    
#Method to insert in the queue(adds to the end)
    def enqueue(self, data):
        self.SongQueue(append)(data)

#Method to take things out of the queue(removes from the front)
    def dequeue(self):
        if self.isempty():
            print("Theres no songs in the Queue!")
            return -1

        print("Removing song...", self.SongQueue[self.front])    
        return self.SongQueue.pop(0)

#Method to check if queue is empty
    def isempty(self):
            return len(self.SongQueue) == 0:

#method to returnn the front of the queue
    def thefront(self):
        if self.isempty():
            print("Theres no songs in the Queue!")
        

        return self.SongQueue[self.front]

#Method to return the size of the queue
    def size(self):
        return len(self.SongQueue)


