class botQueue:
    def __init__(self):
        self.front = 0
        self.SongQueue = []

#Method to insert in the queue(adds to the end)
    def enqueue(self,data):
        self.SongQueue.append(data)

#Method to take things out of the queue
    def dequeue(self):
        if len(self.SongQueue) == 0:
            print("There's no song in the queue")
            return 0
        print("Removing song", self.SongQueue[self.front])
        return self.SongQueue.pop(0)

#Method to check of queue is empty 
    def isempty(self):
        if len(self.SongQueue) == 0:
            return True
        return False

#Method to return front of the queue
    def thefront(self):
        if len(self.SongQueue) == 0:
            print("There's no song in the queue")
            return 0
        return self.SongQueue[self.front]

#Method to return size of the queue
    def size(self):
        return len(self.SongQueue)

#Method to get back of queue
    def theback(self):
        if len(self.SongQueue) == 0:
            print("There's no song in the queue")
            return 0
        return self.SongQueue[len(self.SongQueue)]

#Method to clear queue
    def clear(self):
        self.SongQueue = []        

