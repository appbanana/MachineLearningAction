package tree;

import java.util.Comparator;

/**
 * Balance Binary Search Tree
 * Created by apple on 2019/5/13.
 */
public class BBST<E> extends BinarySearchTree<E> {
    public BBST() {
        this(null);
    }

    public BBST(Comparator<E> comparator) {
        super(comparator);
    }

    protected void rotateLeft(Node<E> grand) {

        Node<E> parent = grand.right;
        Node<E> child = parent.left;
        grand.right = child;
        parent.left = grand;

        afterRotate(grand, parent, child);

    }

    protected void rotateRight(Node<E> grand) {
        Node<E> parent = grand.left;
        Node<E> child = parent.right;

        grand.left = child;
        parent.right = grand;

        afterRotate(grand, parent, child);

    }

    protected void afterRotate(Node<E> grand, Node<E> parent, Node<E> child){
        // 让parent 成为新的跟节点
        parent.parent = grand.parent;
        if (grand.isLeftChild()){
            grand.parent.left = parent;
        }else if (grand.isRightChild()){
            grand.parent.right = parent;
        }else {
            root = parent;
        }

        // 更新child的parent
        if (child != null){
            child.parent = grand;
        }
        grand.parent = parent;

//        // 更新高度
//        updateHeight(grand);
//        updateHeight(parent);
    }

}
