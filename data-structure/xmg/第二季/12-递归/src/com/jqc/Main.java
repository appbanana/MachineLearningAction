package com.jqc;

import com.jqc.graph.Graph;
import com.jqc.graph.Graph.VertexVisit;
import com.jqc.graph.ListGraph;
import com.jqc.graph.Graph.EdgeInfo;
import com.jqc.graph.Graph.WeightManager;
import com.jqc.graph.Graph.PathInfo;

import java.util.List;
import java.util.Map;
import java.util.Set;

public class Main {

    static WeightManager<Double> weightManager = new WeightManager<Double>() {
        @Override
        public int compare(Double w1, Double w2) {
            return Double.compare(w1, w2);
        }

        @Override
        public Double add(Double w1, Double w2) {
            return w1 + w2;
        }

        @Override
        public Double zero() {
            return 0.0;
        }
    };

    public static void main(String[] args) {
        // 测试拓扑
//        testTopo();
        // 测试最小生成树(prim算法, kruskal算法)
//        testMst();

        // 最短路径
//        testSp();

        // 测试多源最短路径
        testMultiSp();
    }

    static void testMultiSp() {
        Graph<Object, Double> graph = directedGraph(Data.NEGATIVE_WEIGHT1);
        Map<Object, Map<Object, PathInfo<Object, Double>>> sp = graph.shortestPath();
        sp.forEach((Object from, Map<Object, PathInfo<Object, Double>> paths) -> {
            System.out.println(from + "---------------------");
            paths.forEach((Object to, PathInfo<Object, Double> path) -> {
                System.out.println(to + " - " + path);
            });
        });

    }

    static void testSp() {
        Graph<Object, Double> graph = directedGraph(Data.NEGATIVE_WEIGHT1);
        Map<Object, PathInfo<Object, Double>> sp = graph.shortestPath("A");

//        Graph<Object, Double> graph = directedGraph(Data.NEGATIVE_WEIGHT2);
//        Map<Object, PathInfo<Object, Double>> sp = graph.shortestPath(0);
        if (sp == null) return;
        sp.forEach((Object v, PathInfo<Object, Double> path) -> {
            System.out.println(v + " - " + path);
        });
    }

    /**
     * 测试拓扑算法
     */
    static void testTopo() {
        Graph<Object, Double> graph = directedGraph(Data.TOPO);
        List<Object> list = graph.topologicalSort();
        System.out.println(list);

    }

    /**
     * 测试最小生成树
     *         prim算法
     *         EdgeInfo{from=2, to=4, weight=4.0}
     *         EdgeInfo{from=5, to=1, weight=1.0}
     *         EdgeInfo{from=0, to=2, weight=2.0}
     *         EdgeInfo{from=7, to=3, weight=9.0}
     *         EdgeInfo{from=2, to=5, weight=3.0}
     *         EdgeInfo{from=5, to=6, weight=4.0}
     *         EdgeInfo{from=5, to=7, weight=5.0}
     *         kruskal算法生成树
     *         EdgeInfo [from=7, to=5, weight=5.0]
     *         EdgeInfo [from=1, to=2, weight=3.0]
     *         EdgeInfo [from=5, to=6, weight=4.0]
     *         EdgeInfo [from=3, to=7, weight=9.0]
     *         EdgeInfo [from=2, to=0, weight=2.0]
     *         EdgeInfo [from=2, to=4, weight=4.0]
     *         EdgeInfo [from=1, to=5, weight=1.0]
     *
     */
    static void testMst() {
        Graph<Object, Double> graph = undirectedGraph(Data.MST_01);
        Set<EdgeInfo<Object, Double>> infos = graph.mst();
        for (EdgeInfo<Object, Double> info : infos) {
            System.out.println(info);
        }
    }


    /**
     * 有向图
     */
    private static  Graph<Object, Double> directedGraph(Object[][] data) {
        Graph<Object, Double> graph = new ListGraph<>(weightManager);
        for (Object[] edge : data) {
            if (edge.length == 1) {
                graph.addVertex(edge[0]);
            } else if (edge.length == 2) {
                graph.addEdge(edge[0], edge[1]);
            } else if (edge.length == 3) {
                double weight = Double.parseDouble(edge[2].toString());
                graph.addEdge(edge[0], edge[1], weight);
            }
        }
        return graph;
    }

    /**
     * 无向图
     * @param data
     * @return
     */
    private static Graph<Object, Double> undirectedGraph(Object[][] data) {
        Graph<Object, Double> graph = new ListGraph<>(weightManager);
        for (Object[] edge : data) {
            if (edge.length == 1) {
                graph.addVertex(edge[0]);
            } else if (edge.length == 2) {
                graph.addEdge(edge[0], edge[1]);
                graph.addEdge(edge[1], edge[0]);
            } else if (edge.length == 3) {
                double weight = Double.parseDouble(edge[2].toString());
                graph.addEdge(edge[0], edge[1], weight);
                graph.addEdge(edge[1], edge[0], weight);
            }
        }
        return graph;
    }
}
