package com.jqc.model;

public class Person {
    private int age;   // 10  20
    private float height; // 1.55 1.67
    private String name; // "jack" "rose"

    public Person(int age, float height, String name) {
        this.age = age;
        this.height = height;
        this.name = name;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || obj.getClass() != getClass()) return false;
        // 比较成员变量 如果每一个成员变量都相等则相等
        Person person = (Person) obj;
        return person.age == age && person.height == height && person.name == name;
    }

    @Override
    public int hashCode() {
        int hashcode = Integer.hashCode(age);
        hashcode = hashcode * 31 + Float.hashCode(height);
        hashcode = hashcode * 31 + (name == null ? 0 : name.hashCode());
        return hashcode;
    }
}
