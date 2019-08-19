package main

import (
	"fmt"
	"sync"
)

// Node 树的每个节点结构体
type Node struct {
	key   int   // 中序遍历的节点序号
	value int   // 节点存储的值 测试存储为int可为任何类型
	left  *Node // 左子节点
	right *Node // 右子节点
}

// ItemBinarySearchTree 树结构体
type ItemBinarySearchTree struct {
	root *Node        // 树的每个节点
	lock sync.RWMutex //互斥锁
}

// Insert 向二叉搜索树的合适位置插入节点
func (tree *ItemBinarySearchTree) Insert(key int, value int) {
	tree.lock.Lock()
	defer tree.lock.Unlock()
	newNode := &Node{key, value, nil, nil}
	// 初始化树
	if tree.root == nil {
		tree.root = newNode
	} else {
		// 在树中递归查找正确的位置并插入
		insertNode(tree.root, newNode)
	}
}

// insertNode 实现递归插入
func insertNode(node, newNode *Node) {
	// 插入到左子树
	if newNode.key < node.key {
		if node.left == nil {
			node.left = newNode
		} else {
			// 递归查找左边插入
			insertNode(node.left, newNode)
		}
	} else {
		// 插入到右子树
		if node.right == nil {
			node.right = newNode
		} else {
			// 递归查找右边插入
			insertNode(node.right, newNode)
		}
	}
}

// Search 检查序号为 k 的元素在树中是否存在
func (tree *ItemBinarySearchTree) Search(key int) bool {
	tree.lock.RLock()
	defer tree.lock.RUnlock()
	return search(tree.root, key)
}
func search(node *Node, key int) bool {
	if node == nil {
		return false
	}
	// 向左搜索更小的值
	if key < node.key {
		return search(node.left, key)
	}
	// 向右搜索更大的值
	if key > node.key {
		return search(node.right, key)
	}
	return true // key == node.key
}

// Min 获取树中值最小的节点：最左节点
func (tree *ItemBinarySearchTree) Min() *int {
	tree.lock.RLock()
	defer tree.lock.RUnlock()
	node := tree.root
	if node == nil {
		return nil
	}
	for {
		if node.left == nil {
			return &node.value
		}
		node = node.left
	}
}

// Max 获取树中值最大的节点：最右节点
func (tree *ItemBinarySearchTree) Max() *int {
	tree.lock.RLock()
	defer tree.lock.RUnlock()
	node := tree.root
	if node == nil {
		return nil
	}
	for {
		if node.right == nil {
			return &node.value
		}
		node = node.right
	}
}

func main() {
	fmt.Println("Start")
    var Tree ItemBinarySearchTree
    Tree.Insert(1,1) 
    res := Tree.Search(2)
    fmt.Println(res)
}
