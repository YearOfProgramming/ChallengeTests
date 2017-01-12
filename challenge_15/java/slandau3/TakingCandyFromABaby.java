

public class TakingCandyFromABaby<T> {
    public int size = 0;
    public Node current = null;

    private class Node {
        public Node next = null;
        public T data = null;

        public Node(T data) {
            this.data = data;
        }
    }

}