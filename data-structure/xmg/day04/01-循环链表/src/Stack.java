/**
 * Created by apple on 2019/4/25.
 */

//package ;

import com.jqc.ArrayList;
import com.jqc.List;

public class Stack<E> {
    private List<E> list = new ArrayList<>();

    public int size() {
        return list.size();
    }

    public boolean isEmpty() {
        return list.isEmpty();
    }

    public void push(E element) {
         list.add(size(), element);
    }


    public E pop() {
        return list.remove(size() - 1);
    }


    public E top() {
        return list.get(size() - 1);
    }
}
