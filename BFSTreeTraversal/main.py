 #This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from TreeNode import TreeNode


def hasRightChildButNoLeftChild(node: TreeNode):
    return node.leftNode is None and node.rightNode is not None

def hasLeftChildButNoRightChild(node: TreeNode):
    return node.leftNode is not None and node.rightNode is None

def haveNoChildren(node: TreeNode):
    return node.leftNode is None and node.rightNode is None

def populateLevelNodeDict(node: TreeNode, nodesDict):
    if node.level not in nodesDict.keys():
        nodesDict.update({node.level: []})
        nodesDict[node.level].append(node)

def calculateChildNodeLevelsAndPopulateLevelMap(node: TreeNode, nodesDict):
    if node.level not in nodesDict.keys():
        nodesDict.update({node.level: []})
    nodesDict[node.level].append(node)
    parentLevel: int = node.level
    if haveNoChildren(node):
        return
    elif hasLeftChildButNoRightChild(node):
        node.leftNode.level = parentLevel + 1
        calculateChildNodeLevelsAndPopulateLevelMap(node, nodesDict)
        nodesDict[(parentLevel + 1)].append(node.rightNode)
    elif hasRightChildButNoLeftChild(node):
        if nodesDict[(parentLevel + 1)] is None:
            nodesDict[(parentLevel + 1)] = []
        nodesDict[(parentLevel + 1)].append(node.leftNohtNode)
        node.rightNode.level = parentLevel + 1
        calculateChildNodeLevelsAndPopulateLevelMap(node, nodesDict)
    else:
        node.leftNode.level = parentLevel + 1
        calculateChildNodeLevelsAndPopulateLevelMap(node, nodesDict)
        node.rightNode.level = parentLevel + 1
        calculateChildNodeLevelsAndPopulateLevelMap(node, nodesDict)

def populateNodeToLevel(node, nodesDict):
    if node.level not in nodesDict.keys():
        nodesDict.update({node.level: []})
    nodesDict[node.level].append(node)

def bfs(rootNode, nodesDict):
    queue = []
    populateNodeToLevel(rootNode, nodesDict)
    queue.append(rootNode)

    while queue:
        node = queue.pop(0)
        currentLevel = node.level + 1
        if haveNoChildren(node):
            return
        elif hasLeftChildButNoRightChild(node):
            node.leftNode.level = currentLevel
            populateNodeToLevel(node.leftNode, nodesDict)
            nodesDict[currentLevel].append(None)
            queue.append(node.leftNode)

        elif hasRightChildButNoLeftChild(node):
            if nodesDict[currentLevel] is None:
                nodesDict[currentLevel] = []
            nodesDict[currentLevel].append(None)
            node.rightNode.level = currentLevel
            populateNodeToLevel(node.rightNode, nodesDict)
            queue.append(node.rightNode)

        else:
            node.leftNode.level = currentLevel
            populateNodeToLevel(node.leftNode, nodesDict)
            queue.append(node.leftNode)
            node.rightNode.level = currentLevel
            populateNodeToLevel(node.rightNode, nodesDict)
            queue.append(node.rightNode)

def printDisctanceForEachNode(nodes):
    emptyNodeCount: int = 0
    for i in range(0, len(nodes)):
        firstNode = nodes[i]
        if firstNode is not None:
            for j in range(i+1, len(nodes)):
                secondNode = nodes[j]
                if secondNode is not None:
                    print("Distance between node {} and node {} is : {}".format(firstNode.value, secondNode.value, (j - i - 1)))
        else:
            emptyNodeCount = emptyNodeCount + 1
    return emptyNodeCount


def printTreeDetails(nodesDict):
    emptyNodeCount: int = 0
    for level in nodesDict:
        emptyNodesOnLevel = printDisctanceForEachNode(nodesDict[level])
        print("Empty node present on level {} are : {}".format(level, emptyNodesOnLevel))
        emptyNodeCount += emptyNodesOnLevel
    print("Total empty nodes present in tree : " + emptyNodeCount)


rootNode = TreeNode(5)
rootNode.level = 0

node2 = TreeNode(2)
rootNode.leftNode = node2

node3 = TreeNode(3)
rootNode.rightNode = node3

node7 = TreeNode(7)
node2.leftNode = node7

node1 = TreeNode(1)
node3.rightNode = node1

node9 = TreeNode(9)
node7.leftNode = node9

node4 = TreeNode(4)
node1.leftNode = node4

node6 = TreeNode(6)
node1.rightNode = node6

levelNodesDict = {}
bfs(rootNode, levelNodesDict)
printTreeDetails(levelNodesDict);
#calculateChildNodeLevelsAndPopulateLevelMap(rootNode, levelNodesDict)