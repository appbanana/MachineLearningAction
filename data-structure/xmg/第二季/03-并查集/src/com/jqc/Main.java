package com.jqc;
import com.jqc.tools.Times;
import com.jqc.tools.Asserts;
import com.jqc.union.*;

public class Main {
    static final int count = 200000;
    public static void main(String[] args) {
//        test1();
//        test2(new UnionFind_QU(count));
//        test2(new UnionFind_QU_S(count));
        test2(new UnionFind_QU_R(count));
        test2(new UnionFind_QU_R_PC(count));
        test2(new UnionFind_QU_R_PS(count));
        test2(new UnionFind_QU_R_PH(count));
    }

    private static void test1() {
//        UnionFind_QF uf = new UnionFind_QF(12);
//        UnionFind_QU uf = new UnionFind_QU(12);
        UnionFind_QU_S uf = new UnionFind_QU_S(12);
        uf.union(0, 1);
        uf.union(0, 3);
        uf.union(0, 4);
        uf.union(2, 3);
        uf.union(2, 5);

        uf.union(6, 7);

        uf.union(8, 10);
        uf.union(9, 10);
        uf.union(9, 11);

        Asserts.test(!uf.isSame(2, 7));

        uf.union(4, 6);

        Asserts.test(uf.isSame(2, 7));
    }

    private static void test2(UnionFind uf) {
        Times.test(uf.getClass().getSimpleName(), () -> {
            for (int i = 0; i < count; i++) {
                uf.union((int)(Math.random() * count),
                        (int)(Math.random() * count));
            }

            for (int i = 0; i < count; i++) {
                uf.isSame((int)(Math.random() * count),
                        (int)(Math.random() * count));
            }
        });
    }
}
