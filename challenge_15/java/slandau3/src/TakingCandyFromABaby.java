/**
 * Created by slandau on 1/12/17.
 */

/**
 * @author Steven Landau
 * @description TODO
 */
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
            int cur = 1;
            while (cur != size) {
                temp = temp.next;
                cur++;
            }
            temp.next = new Node(data);
            temp.next.next = this.root;
        }
        incrementSize();
    }

    public void printList() {
        if (this.size == 0) {
            System.out.println(this.root.data);
        } else {
            Node temp = this.root.next;
            System.out.println(this.root.data);
            while (temp != this.root) {
                System.out.println(temp.data);
                temp = temp.next;
            }
        }
    }

    /**
     *
     */
    public void removeNode(T data) {
        if (this.root.data == data) {
            Node temp = root;
            while (temp.next.data != data) {
                temp = temp.next;
            }
            this.root = this.root.next;
            temp.next = temp.next.next;
            decrementSize();
        } else {

            int moves = 1;

            Node temp = this.root;
            while (moves <= this.size) {
                if (temp.next.data == data) {
                    temp.next = temp.next.next;
                    decrementSize();
                    return;
                }
                moves++;
                temp = temp.next;
            }
            // If we got here, then the data is not in the list
            throw new IndexOutOfBoundsException(data + " not found in the linked list");
        }
    }

    public T beginTheft() { // this destroys the list
        if (size == 1 || size == 0) {
            System.out.println("not enough kids to steal from");
            return null;
        } else {
            int current = 1;
            while(size > 1) {
                //System.out.println(temp.data);
                if (current % 2 == 0) {
                    removeNode(root.data);
                }
                root = root.next;

                current++;
            }
            System.out.println(root.data);
            return root.data;
        }
    }

    public static void main(String[] args) {
        TakingCandyFromABaby<Integer> a = new TakingCandyFromABaby<>();
        a.append(1);
        a.append(2);
        a.append(3);
        a.append(4);
        //a.removeNode(1);
        //a.removeNode(3);
        //a.printList();
        a.beginTheft();
    }
}
