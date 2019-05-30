package com.jqc.set;
import com.jqc.map.LinkedHashMap;
import com.jqc.map.Map;

public class LinkedHashSet<E> implements Set<E> {

    LinkedHashMap<E, Object> linkMap = new LinkedHashMap<>();

    @Override
    public int size() {
        return linkMap.size();
    }

    @Override
    public boolean isEmpty() {
        return linkMap.isEmpty();
    }

    @Override
    public void clear() {
        linkMap.clear();
    }

    @Override
    public boolean contains(E element) {
        return linkMap.containsKey(element);
    }

    @Override
    public void add(E element) {
        linkMap.put(element, null);
    }

    @Override
    public void remove(E element) {
        linkMap.remove(element);
    }

    @Override
    public void traversal(Visitor<E> visitor) {
        linkMap.traversal(new Map.Visitor<E, Object>() {
            public  boolean visit(E key, Object valuet){
                return visitor.visit(key);
            }

        });
    }
}
