package com.jqc.graph;


import java.util.*;

/**
 * @author appbanana
 * @date 2019/11/2
 */
public class ListGraph<V, E> implements Graph<V, E> {
    // 顶点的map key: value ---> V:Vertex
    private Map<V, Vertex<V, E>> vertices = new HashMap<>();
    // 存储边的容器
    private Set<Edge<V, E>> edges = new HashSet<>();


    @Override
    public int edgesSize() {
        return edges.size();
    }

    @Override
    public int verticesSize() {
        return vertices.size();
    }

    /**
     * 添加顶点
     * @param v 外界传过来的点
     */
    @Override
    public void addVertex(V v) {
        // 如果vertices里面包含这个v, 说明已经添加过了, 不需要重复添加
        if (vertices.containsKey(v)) return;
        // 将外界传过来的点包装成Vertex
        Vertex<V, E> vertex = new Vertex<>(v);
        vertices.put(v, vertex);

    }

    /**
     * 添加边
     * @param from 进边
     * @param to 出边
     */
    @Override
    public void addEdge(V from, V to) {
        addEdge(from, to, null);
    }

    /**
     * 添加边
     * @param from 进边
     * @param to 出边
     * @param weight 边权重
     */
    @Override
    public void addEdge(V from, V to, E weight) {
        // 根据起始点(from)获取其对应的顶点(Vertex)
        Vertex<V, E> fromVertex = vertices.get(from);
        if (fromVertex == null) {
            // 如果为空, 说明之前没有存储过, 接下来创建, 并添加到vertices(这是个map)中
            fromVertex = new Vertex<>(from);
            vertices.put(from, fromVertex);
        }

        Vertex<V, E> toVertex = vertices.get(to);
        if (toVertex == null) {
            toVertex = new Vertex<>(to);
            vertices.put(to, toVertex);
        }

        // 根据起始点, 终点创建边 并添加到集合中
        Edge<V, E> edge = new Edge<>(fromVertex, toVertex);
        edge.weight = weight;

        // 如果remove返回结果为true, 说明之前存储过;为false, 说明之前没有存储过
        // 不这样搞的话到时你需要遍历fromVertex.outEdges, toVertex.inEdges找到这条边,更新weight,
        // 这样搞的好处就是我不需要遍历, 先删除在添加
        if (fromVertex.outEdges.remove(edge)) {
            toVertex.inEdges.remove(edge);
            edges.remove(edge);
        }

        edges.add(edge);
        // 将创建的边添加到起始点的出边的集合上
        fromVertex.outEdges.add(edge);
        // 将创建的边添加到终点点的进边的集合上
        toVertex.inEdges.add(edge);
    }

    /**
     * 删除顶点, 需要把这个点进边和出边包含所有的信息全删掉
     * @param v 顶点
     */
    @Override
    public void removeVertex(V v) {
        Vertex<V, E> vertex = vertices.get(v);
        if (vertex == null) return;
        // 不能边遍历边删除, 会出问题的, 可以借助Iterator来实现
        for (Iterator<Edge<V, E>> iterator = vertex.outEdges.iterator(); iterator.hasNext();) {
            Edge<V, E> edge = iterator.next();
            // edge.to 拿到这条边的终点 然后在终点中进边集合中删除这条边
            edge.to.inEdges.remove(edge);
            // 将当前遍历到的元素edge从集合vertex.outEdges中删掉
            iterator.remove();
            edges.remove(edge);
        }

        // 大前提 目标点的进边集合中遍历
        for (Iterator<Edge<V, E>> iterator = vertex.inEdges.iterator(); iterator.hasNext();) {
            Edge<V, E> edge = iterator.next();
            // edge.from 拿到这条边的起始点 然后在起始点中出边集合中删除这条边
            edge.from.outEdges.remove(edge);
            // 将当前遍历到的元素edge从集合vertex.inEdges中删掉
            iterator.remove();
            edges.remove(edge);
        }

    }

    /**
     * 删除边
     * @param from 起始点
     * @param to 终点
     */
    @Override
    public void removeEdge(V from, V to) {
        Vertex<V, E> fromVertex = vertices.get(from);
        if (fromVertex == null) return;

        Vertex<V, E> toVertex = vertices.get(to);
        if (toVertex == null) return;

        Edge<V, E> edge = new Edge<>(fromVertex, toVertex);
        // 这个删除很巧 如果删除返回true 说明删除成功, 同时toVertex.inEdges和edges都需要删除这条边
        // 如果返回false 不需要做任何处理
        if (fromVertex.outEdges.remove(edge)) {
            toVertex.inEdges.remove(edge);
            edges.remove(edge);
        }

    }

    /**
     * 自定义输出
     */
    public void print() {
        vertices.forEach((V v, Vertex<V, E> vertex) -> {
            System.out.println(v);
            System.out.println("out-------out---------out");
            System.out.println(vertex.outEdges);
            System.out.println("in-------in---------in");
            System.out.println(vertex.inEdges);
        });

        System.out.println("==========================");
        edges.forEach((Edge<V, E> edge) -> {
            System.out.println(edge);
        });
    }

    // 顶点类
    private static class Vertex<V, E> {
        V value;
        // 顶点的进边
        Set<Edge<V, E>> inEdges = new HashSet<>();
        // 顶点的出边
        Set<Edge<V, E>> outEdges = new HashSet<>();

        Vertex(V value) {
            this.value = value;
        }

        @Override
        public boolean equals(Object obj) {
            return Objects.equals(value, ((Vertex) obj).value);
        }

        @Override
        public int hashCode() {
            return value == null ? 0 : value.hashCode();
        }

        @Override
        public String toString() {
            return value == null ? "null" : value.toString();
        }
    }

    private static class Edge<V, E> {
        // 边的起始点
        Vertex<V, E> from;
        // 边的终点
        Vertex<V, E> to;
        // 边权重
        E weight;

        /**
         * 边的构造器初始化
         * @param from 起始点
         * @param to 终点
         */
        public Edge(Vertex<V, E> from, Vertex<V, E> to) {
            this.from = from;
            this.to = to;
        }

        @Override
        public boolean equals(Object obj) {
            Edge edg = (Edge) obj;
            return Objects.equals(from, edg.from) && Objects.equals(to, edg.to);
        }

        @Override
        public int hashCode() {
            return from.hashCode() * 31 + to.hashCode();
        }

        @Override
        public String toString() {
            return "Edge [from=" + from + ", to=" + to + ", weight=" + weight + "]";
        }
    }
}
