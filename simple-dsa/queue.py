class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, ele):
        self.queue.append(ele)

    def dequeue(self):

        if len(self.queue) == 0:
            return "Underflow Error: Cant evaluate the queue"

        # removed_element = self.queue[0]
        # self.queue = self.queue[1:]
        removed_element = self.queue.pop(0)

        return f"Removed element is: {removed_element}"

def main():

    q = Queue()

    q.enqueue(23)
    q.enqueue(45)
    q.enqueue(56)
    q.enqueue(34)
    q.enqueue(1)

    print(f"Queue: {q.queue}")

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
 
    print(f"New Queue: {q.queue}")

main()
