# Problem: Implement Queue using Two Stacks

# -------------------------------------------------------------
# Queue (FIFO) using two stacks (LIFO)

class Queue:
    def __init__(self):
        self.in_stack = []   # used for enqueue
        self.out_stack = []  # used for dequeue

    # ---------------------------------------------------------
    # Enqueue operation (push to in_stack)
    def enqueue(self, x):
        self.in_stack.append(x)

    # ---------------------------------------------------------
    # Dequeue operation (pop from out_stack)
    def dequeue(self):
        # If out_stack is empty, transfer elements
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        if not self.out_stack:
            raise IndexError("Queue is empty")

        return self.out_stack.pop()

    # ---------------------------------------------------------
    # Peek front element
    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        if not self.out_stack:
            raise IndexError("Queue is empty")

        return self.out_stack[-1]

    # ---------------------------------------------------------
    # Check if queue is empty
    def empty(self):
        return not self.in_stack and not self.out_stack


# -------------------------------------------------------------
# Main function (example usage)
def main():
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Front element:", q.peek())  # 10

    print("Dequeued:", q.dequeue())    # 10
    print("Dequeued:", q.dequeue())    # 20

    q.enqueue(40)

    print("Front element:", q.peek())  # 30
    print("Dequeued:", q.dequeue())    # 30
    print("Dequeued:", q.dequeue())    # 40

    print("Is queue empty?", q.empty())  # True


# -------------------------------------------------------------
if __name__ == "__main__":
    main()


# -------------------------------------------------------------
# Complexity Analysis:
#
# Enqueue:
# O(1)
#
# Dequeue:
# Amortized O(1)
# - Each element is moved at most once from in_stack to out_stack
#
# Peek:
# Amortized O(1)
#
# Space Complexity:
# O(n)
#
# -------------------------------------------------------------
# Key Insight:
# - in_stack → collects elements
# - out_stack → serves elements
# - Transfer reverses order → FIFO behavior
#
# -------------------------------------------------------------
# Interview Tip:
# Say:
# "Each element is pushed and popped at most once,
# so operations are amortized O(1)."