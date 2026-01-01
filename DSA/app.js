function createCircularQueue(size) {
  let queue = new Array(size);
  let front = -1;
  let rear = -1;

  function isFull() {
    return (rear + 1) % size === front;
  }

  function isEmpty() {
    return front === -1;
  }

  function enqueue(element) {
    if (isFull()) {
      throw new Error('Queue is full');
    }

    if (isEmpty()) {
      front = 0;
    }

    rear = (rear + 1) % size;
    queue[rear] = element;
  }

  function dequeue() {
    if (isEmpty()) {
      throw new Error('Queue is empty');
    }

    const element = queue[front];

    if (front === rear) {
      front = -1;
      rear = -1;
    } else {
      front = (front + 1) % size;
    }

    return element;
  }

  function display() {
    if (isEmpty()) {
      console.log('Queue is empty');
      return;
    }

    let i = front;
    let result = '';

    while (true) {
      result += queue[i] + ' ';
      if (i === rear) break;
      i = (i + 1) % size;
    }

    console.log(result.trim());
  }

  return {
    enqueue,
    dequeue,
    isFull,
    isEmpty,
    display,
  };
}

const cq = createCircularQueue(5);
cq.enqueue(10);
cq.enqueue(20);
cq.enqueue(30);
cq.enqueue(40);
cq.enqueue(50);

cq.display();

console.log(cq.dequeue());
cq.display();

cq.enqueue(60);
cq.display();

console.log(cq.isFull());
console.log(cq.isEmpty());

