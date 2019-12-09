package com.jqc.graph;

import com.jqc.heap.MinHeap;
import com.jqc.union.GenericUnionFind;

import java.util.*;

/**
 * 邻接表
 * @author appbanana
 * @date 2019/11/2
 */
public class ListGraph<V, E> extends Graph<V, E> {
    // 顶点的map key: value ---> V:Vertex
    private Map<V, Vertex<V, E>> vertices = new HashMap<>();
    // 存储边的容器
    private Set<Edge<V, E>> edges = new HashSet<>();

    // 边权重比较器
    private Comparator<Edge<V, E>> edgeComparator = (Edge<V, E> e1, Edge<V, E> e2) -> {
        return weightManager.compare(e1.weight, e2.weight);
    };



    public ListGraph() {
    }

    public ListGraph(WeightManager<E> weightManager) {

        super(weightManager);
    }

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
     * 深度遍历
     * 思路:其实跟二叉树的层序遍历很像
     * @param begin 开始点
     */
    @Override
    public void bfs(V begin, VertexVisit visitor) {
        Vertex<V, E> beginVertex = vertices.get(begin);
        if (beginVertex == null) return;
        Queue<Vertex<V, E>> queue = new LinkedList<>();
        HashSet<Vertex<V, E>> visitedVertices = new HashSet<>();
        queue.offer(beginVertex);
        visitedVertices.add(beginVertex);

        while (!queue.isEmpty()) {
            Vertex<V, E> vertex = queue.poll();
            if (visitor.visit(vertex.value)) return;

            for (Edge<V, E> edge : vertex.outEdges) {
                if (visitedVertices.contains(edge.to)) continue;
                queue.offer(edge.to);
                visitedVertices.add(edge.to);
            }
        }

    }

    /**
     * 深度遍历
     * 思路:类比二叉树的前序遍历
     * @param begin 气起始点
     */
    @Override
    public void dfs(V begin, VertexVisit visitor) {
        Vertex<V, E> beginVertex = vertices.get(begin);
        if (beginVertex == null) return;

        dfs(beginVertex, new HashSet<>(), visitor);

    }

    /**
     * 深度遍历 非递归来实现
     * 思路:仿照二叉树的前序遍历来实现
     * @param begin 气起始点
     */
    public void dfs1(V begin, VertexVisit visitor) {
        Vertex<V, E> beginVertex = vertices.get(begin);
        if (beginVertex == null) return;

        Stack<Vertex<V, E>> stack = new Stack<>();
        HashSet<Vertex<V, E>> visitedVertex = new HashSet<>();
        stack.push(beginVertex);
        visitedVertex.add(beginVertex);
        if (visitor.visit(beginVertex.value)) return;

        while (!stack.isEmpty()) {
            Vertex<V, E> vertex = stack.pop();
            for (Edge<V, E> edge : vertex.outEdges) {
                if (visitedVertex.contains(edge.to)) continue;
                // 我感觉这个可以不写
                stack.push(edge.from);
                stack.push(edge.to);
                visitedVertex.add(edge.to);
                if (visitor.visit(edge.to.value)) return;
                break;
            }
        }

    }

    private void dfs(Vertex<V,E> vertex, HashSet<Vertex<V, E>> visitedVertex, VertexVisit visitor) {
        if (vertex == null) return;
        if (visitor.visit(vertex.value)) return;
        visitedVertex.add(vertex);
        // 遍历该顶点的出边集合中to顶点
        for (Edge<V, E> edge : vertex.outEdges) {
            if (visitedVertex.contains(edge.to)) continue;
            dfs(edge.to, visitedVertex, visitor);
        }
    }

    /**
     * 卡恩拓扑算法
     * @return
     */
    @Override
    public List<V> topologicalSort() {
        List<V> list = new ArrayList<>();
        Queue<Vertex<V, E>> queue = new LinkedList<>();
        HashMap<Vertex<V, E>, Integer> ins = new HashMap<>();

        vertices.forEach((V v, Vertex<V, E> vertex) -> {
            int inSize = vertex.inEdges.size();
            if (inSize == 0) {
                // 入度为0添加到队列中
                queue.offer(vertex);
            }else {
                // 入度不为0, 记录该顶点的入度大小
                ins.put(vertex, inSize);
            }
        });
        while (!queue.isEmpty()) {
            Vertex<V, E> vertex = queue.poll();
            list.add(vertex.value);
            // 遍历这个顶点的出边
            for (Edge<V, E> edge : vertex.outEdges) {
                // 由边的终点获取map中对应的size, 实际上获取该边终点的入度
                int inSize = ins.get(edge.to) - 1;
                if (inSize == 0) {
                    // 入度为0 添加到队列中
                    queue.offer(edge.to);
                }else {
                    // 入度不为0, 更新该边终点对应的入度大小
                    ins.put(edge.to, inSize);
                }
            }
        }
        return list;
    }

    @Override
    public Set<EdgeInfo<V, E>> mst() {
        return prim();
//        return kruskal();
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

    /**
     * prim算法, 最小切分定理 在边to顶点所有的出边中 挑选权重比较小的边
     * @return
     */
    private Set<EdgeInfo<V, E>> prim() {
        Iterator<Vertex<V, E>> it = vertices.values().iterator();
        if (!it.hasNext()) return null;
        // 存放边信息
        Set<EdgeInfo<V, E>> edgeInfos = new HashSet<>();
        // 存放已经添加的顶点信息
        Set<Vertex<V, E>> addedVertex = new HashSet<>();

        // 获取迭代器中的第一个元素
        Vertex<V, E> vertex = it.next();
        // 并将顶点添加到集合中
        addedVertex.add(vertex);
        // 批量建堆
        MinHeap<Edge<V, E>> heap =  new MinHeap(vertex.outEdges, edgeComparator);

        int verticesSize = vertices.size();
        while (!heap.isEmpty() && addedVertex.size() < verticesSize) {
            Edge<V, E> edge = heap.remove();
            if (addedVertex.contains(edge.to)) continue;
            // 把边转化为EdgeInfo,并添加到集合中
            edgeInfos.add(edge.info());
            // 将边终点添加到集合中(addedVertex)
            addedVertex.add(edge.to);
            // 把边终点的所有出边添加到堆里面
            heap.addAll(edge.to.outEdges);
        }

        return edgeInfos;
    }

    /**
     * 最小生成树 kruskal算法生成最小生成树
     *  按边的权重从小到大依次加入 但不能形成还, 直到加入n - 1条边为之
     * @return
     */
    private Set<EdgeInfo<V, E>> kruskal() {
        // 边的长度为所有顶点数量减1
        int edgeSize = vertices.size() - 1;
        if (edgeSize < 1) return null;

        Set<EdgeInfo<V, E>> edgeInfos = new HashSet<>();
        // 所有的边批量建堆
        MinHeap<Edge<V, E>> heap = new MinHeap<>(edges, edgeComparator);
        GenericUnionFind<Vertex<V, E>> uf = new GenericUnionFind<>();
        // vertice是所有的顶点集合, 使用并查集是为了判断他们会不会形成闭环
        vertices.forEach((V v, Vertex<V, E> vertex) -> {
            uf.makeSet(vertex);
        });
        while (!heap.isEmpty() && edgeInfos.size() < edgeSize) {
            Edge<V, E> edge = heap.remove();
            if (uf.isSame(edge.from, edge.to)) continue;

            edgeInfos.add(edge.info());
            uf.union(edge.from, edge.to);
        }
        return edgeInfos;
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

        EdgeInfo<V, E> info() {
            return new EdgeInfo<>(from.value, to.value, weight);
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
