# 📌 Singly Linked List – Complete Guide

## 📖 What is a Singly Linked List?

A **Singly Linked List (SLL)** is a linear data structure where each element (node) contains:

* **Data**
* **Pointer (next)** → points to the next node

👉 Unlike arrays:

* Dynamic size
* Non-contiguous memory
* Sequential access

---

## 🧠 Basic Structure

![Singly Linked List](https://media.geeksforgeeks.org/wp-content/uploads/20240219155344/Singly-Linked-List.webp)

Each node looks like:

```
[data | next]
```

---

## 🏗️ Node Class (Python)
- A **Node** is the fundamental building block of a linked list. Each node is a self-contained unit that stores:

- Data → the actual value
- Next Pointer → a reference to the next node in the sequence

#### In a singly linked list:

- The first node is called the head
- The last node points to None, indicating the end of the list
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

## 🚶 Traversal (Display Linked List)

- **Traversal** means visiting each node in the linked list sequentially, starting from the head and moving towards the end.

#### 👉 How it works:

- Start from the head node
- Follow the next pointer
- Continue until None is reached

#### 👉 Key Points:

- Traversal is linear (O(n))
- No random access (unlike arrays)
- Used in almost every operation (search, insert, delete)


```python
def traverse(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
```

---

## ➕ Insertion Operations

### 1. Insert at Beginning
- New node becomes the new head
- Its `next` points to the old head
- Time Complexity: O(1)

```python
def insert_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node
```

---

### 2. Insert at End

- Traverse to the last node
- Update its `next` to the new node
- Time Complexity: **O(n)**

```python
def insert_end(head, data):
    new_node = Node(data)
    
    if not head:
        return new_node
    
    current = head
    while current.next:
        current = current.next
    
    current.next = new_node
    return head
```

---

### 3. Insert at Position

- Traverse to the desired position
- **Adjust pointers:**
- New node points to next node
- Previous node points to new node
- Time Complexity: **O(n)**

#### 👉 Key Insight:

>Insertion is mainly about **pointer manipulation**, not shifting elements like arrays.

```python
def insert_position(head, data, pos):
    new_node = Node(data)
    
    if pos == 0:
        new_node.next = head
        return new_node
    
    current = head
    for _ in range(pos - 1):
        current = current.next
    
    new_node.next = current.next
    current.next = new_node
    return head
```

---

## ❌ Deletion Operations

### 1. Delete from Beginning

- Move `head` to the`next` node
- Time Complexity: **O(1)**

```python
def delete_beginning(head):
    if not head:
        return None
    return head.next
```

---

### 2. Delete from End

- Traverse to second last node
- Set its `next` to `None`
- Time Complexity: **O(n)**

```python
def delete_end(head):
    if not head or not head.next:
        return None
    
    current = head
    while current.next.next:
        current = current.next
    
    current.next = None
    return head
```

---

### 3. Delete by Value

- Find the `node` with the `target` value

- Update previous node’s next to skip it

- Time Complexity: **O(n)**

#### 👉 Key Insight: Deletion requires careful handling of pointers to avoid
- Losing the list
- Breaking the chain

```python
def delete_value(head, key):
    if head and head.data == key:
        return head.next
    
    current = head
    while current.next and current.next.data != key:
        current = current.next
    
    if current.next:
        current.next = current.next.next
    
    return head
```

---

## 🔍 Search in Linked List

- Start from the head node
- Compare current.data with the key
- If match → return True
- Else → move to current.next
- **Repeat until:**
- `Found ✅`
- `Or reached None ❌`

```python
def search(head, key):
    current = head
    while current:
        if current.data == key:
            return True
        current = current.next
    return False
```

---

## 📏 Length of Linked List

- Initialize a counter → `count = 0`
- Start from the **head node**
- Move through each node using `next`
- Increment count for every node
- Stop when `current == None`

```python
def length(head):
    count = 0
    current = head
    
    while current:
        count += 1
        current = current.next
    
    return count
```

---

## 🔄 Example Usage

```python
head = None

head = insert_beginning(head, 3)
head = insert_beginning(head, 1)
head = insert_end(head, 5)

traverse(head)  # Output: 1 -> 3 -> 5 -> None

head = delete_value(head, 3)
traverse(head)  # Output: 1 -> 5 -> None
```

---

## ⚡ Key Concepts Summary

| Concept   | Explanation         |
| --------- | ------------------- |
| Head      | Starting node       |
| Node      | Data + next pointer |
| Traversal | Visiting all nodes  |
| Insertion | Adding nodes        |
| Deletion  | Removing nodes      |

---

## 🚫 Common Mistakes

* Forgetting to update `next` pointer
* Losing reference to head
* Not handling empty list

---

## 🎯 Practice Next

* Reverse Linked List
* Detect Cycle
* Find Middle Node
* Merge Lists

---

## 📌 Conclusion

Mastering **Singly Linked List** builds strong fundamentals for:

* Data Structures
* Interviews
* Advanced topics like Trees & Graphs

---
