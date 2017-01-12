

public class TakingCandyFromABaby<T> {
    private int size = 0;
    public Node root = null;

    private class Node {
        public Node next = null;
        public T data = null;

        public Node(T data) {
            this.data = data;
        }
    }

    private void incrementSize() {
        this.size++;
    }

    private void decrementSize() {
        this.size--;
    }

    public void append(T data) {
        if (size == 0) {
            this.root = new Node(data);
        } else {
            Node temp = this.root;
            int cur = 0;
            while (cur != size) {
                temp = temp.next;
            }
            temp.next = new Node(data);
            temp.next.next = this.root;
        }
        incrementSize();
    }

    public void printList() {
        Node temp = this.root;
        while (temp != null) {
            System.out.println(temp.data);
            temp = temp.next;
        }
    }

    public T removeNode(T data) {
        }
        
    }
}