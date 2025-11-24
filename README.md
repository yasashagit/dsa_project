# mplementation and Analysis of Data Structures and Algorithms

**Authors:** Eduard Rednic, Oleksandr Yakovlev

**Language:** Python 3

**Main Notebook:** `Demo_file.ipynb`

## 📋 Project Overview

This project explores the design, implementation, and practical analysis of fundamental data structures and algorithms in Python. Unlike standard library implementations, this project builds these structures from scratch to provide a deep understanding of their internal mechanics, memory management, and time complexity.

The project emphasizes **Big O analysis**, using empirical data and visualizations (Matplotlib) to demonstrate the performance differences between various algorithms (e.g., $O(n)$ vs $O(\log n)$).

## 🛠 Features & Implementations

### 1. Data Structures

-   **Linear Structures:**
    
    -   **Dynamic Arrays & Lists:** Custom implementation of resizeable arrays.
        
    -   **Linked Lists:** Singly and Doubly Linked Lists.
        
    -   **Stacks & Queues:** LIFO and FIFO structures implemented via linked nodes.
        
-   **Non-Linear Structures:**
    
    -   **Hash Tables:** Implementation using **Chaining** for collision handling. Includes custom hash functions and dynamic resizing.
        
    -   **Binary Trees:** General tree structures.
        
    -   **Binary Search Trees (BST):** Ordered trees with recursive insertion/deletion.
        
    -   **AVL Trees:** Self-balancing binary search trees ensuring $O(\log n)$ lookup times.
        

### 2. Algorithms

-   **Sorting:**
    
    -   Bubble Sort ($O(n^2)$)
        
    -   Insertion Sort ($O(n^2)$)
        
    -   Merge Sort ($O(n \log n)$)
        
-   **Searching:**
    
    -   Linear Search ($O(n)$)
        
    -   Binary Search ($O(\log n)$) - Recursive and Iterative approaches.
        
-   **Tree Traversals:**
    
    -   Depth-First: Pre-order, In-order, Post-order.
        
    -   Breadth-First: Level-order traversal.
        

## 📊 Performance Analysis & Visualization

This project relies heavily on **Matplotlib** to generate performance graphs and **Graphviz** to visualize tree structures.

**Key Comparisons:**

-   **Sorting Benchmarks:** Comparing execution time of Bubble Sort vs. Merge Sort on datasets ranging from 100 to 2,000 elements.
    
-   **Search Efficiency:** Visualizing the massive efficiency gap between Linear Search and Binary Search (Log-scale analysis).
    
-   **Hash Table Performance:** Demonstrating constant time $O(1)$ lookups vs. linear list scanning.
    
-   **Tree Visualization:** Generating SVG diagrams of BST and AVL trees to visually verify structure and balancing rotations.
    

## 📂 Project Structure

Plaintext

```
├── dsa/                     # Source code for data structures
│   ├── linked_list.py
│   ├── stack_queue.py
│   ├── hashtable.py         # Hash Table with Chaining
│   └── trees.py             # BST and AVL implementations
├── Demo_file.ipynb          # Main Jupyter Notebook (Demos & Benchmarks)
├── README.md                # Project Documentation
├── requirements.txt         # Dependencies
└── images/                  # Generated graphs and visualizations

```

## 🚀 Getting Started

### Prerequisites

-   Python 3.8+
    
-   Jupyter Notebook
    

### Installation

1.  Clone the repository or download the files.
    
2.  Install the required Python libraries:
    
    Bash
    
    ```
    pip install matplotlib graphviz jupyter
    
    ```
    
3.  **Graphviz Setup:**
    
    -   To render tree diagrams, you must install the Graphviz **system executable** (not just the Python library).
        
    -   **Windows:** Download the installer from [graphviz.org](https://graphviz.org/download/) and check **"Add to PATH"** during installation.
        
    -   **Mac:** `brew install graphviz`
        
    -   **Linux:** `sudo apt-get install graphviz`
        

### Running the Project

Open the main notebook to see the code in action:

Bash

```
jupyter notebook Demo_file.ipynb

```

## 🧪 Usage Examples

**Binary Search Usage:**

Python

```
from dsa.searching import binary_search

arr = [1, 3, 5, 7, 9, 11]
index = binary_search(arr, 7)
print(f"Found 7 at index: {index}")

```

**AVL Tree Visualization:**

Python

```
from dsa.trees import AVLTree

avl = AVLTree()
for lang in ["Python", "Java", "C++"]:
    avl.insert(lang)

# Generates a visual diagram of the balanced tree
avl.visualize() 

```

## 📈 Conclusion

Through this project, we demonstrated that while simple structures (like Lists or Linear Search) are easier to implement, they often lack scalability. Advanced structures like **Hash Tables** and **AVL Trees** introduce complexity in implementation but provide necessary efficiency ($O(1)$ or $O(\log n)$) for large-scale applications.