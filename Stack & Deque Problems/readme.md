# 🚀 Stack + Queue + Deque — 60 LeetCode Problems

## 🧠 Stack → Monotonic Stack → Queue → Deque

A focused **60-problem roadmap** for mastering stack, queue, and deque patterns for coding interviews.

**Main goal:** recognize when LIFO, FIFO, monotonic ordering, or a deque-based sliding window can simplify a problem.

---

## 🎯 Challenge Statistics

| Category | Total | Easy | Medium | Hard |
|:--|--:|--:|--:|--:|
| Stack | **40** | **8** | **28** | **4** |
| Queue + Deque | **20** | **4** | **14** | **2** |
| **Total** | **60** | **12** | **42** | **6** |

| Difficulty | Count | Percentage |
|:--|--:|--:|
| 🟢 Easy | **12** | **20%** |
| 🟡 Medium | **42** | **70%** |
| 🔴 Hard | **6** | **10%** |

**Daily target:** 2 problems per day × 30 days = 60 practice slots.

---


## Phase 1 — Stack Fundamentals

**Goal:** Understand LIFO, matching parentheses, basic stack operations, and stack-based string processing.

| Done | # | LeetCode Problem | Difficulty | Pattern / Focus |
|:--:|--:|:--|:--:|:--|
| [x] | 1 | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | 🟢 Easy | Matching parentheses |
| [ ] | 2 | [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | 🟢 Easy | Next greater element |
| [ ] | 3 | [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) | 🟢 Easy | Stack implementation |
| [ ] | 4 | [1047. Remove All Adjacent Duplicates in String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) | 🟢 Easy | String + stack |
| [ ] | 5 | [1544. Make The String Great](https://leetcode.com/problems/make-the-string-great/) | 🟢 Easy | Adjacent cancellation |
| [ ] | 6 | [1021. Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/) | 🟢 Easy | Parentheses depth |
| [ ] | 7 | [682. Baseball Game](https://leetcode.com/problems/baseball-game/) | 🟢 Easy | Stack simulation |
| [ ] | 8 | [155. Min Stack](https://leetcode.com/problems/min-stack/) | 🟡 Medium | Auxiliary stack / design |

**Concept checklist**

- [ ] LIFO principle and stack operations
- [ ] Matching and validating parentheses
- [ ] Using a stack to process strings
- [ ] Maintaining extra state in a stack

**Notes / mistakes to revisit:**

```text

```

---

## Phase 2 — Expression Evaluation & Stack Simulation

**Goal:** Process expressions, nested structures, and stateful simulations.

| Done | # | LeetCode Problem | Difficulty | Pattern / Focus |
|:--:|--:|:--|:--:|:--|
| [ ] | 9 | [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | 🟡 Medium | Expression evaluation |
| [ ] | 10 | [71. Simplify Path](https://leetcode.com/problems/simplify-path/) | 🟡 Medium | Path normalization |
| [ ] | 11 | [394. Decode String](https://leetcode.com/problems/decode-string/) | 🟡 Medium | Nested encoding |
| [ ] | 12 | [227. Basic Calculator Ii](https://leetcode.com/problems/basic-calculator-ii/) | 🟡 Medium | Operator precedence |
| [ ] | 13 | [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | 🟡 Medium | Collision simulation |
| [ ] | 14 | [402. Remove K Digits](https://leetcode.com/problems/remove-k-digits/) | 🟡 Medium | Greedy + monotonic stack |
| [ ] | 15 | [946. Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/) | 🟡 Medium | Stack simulation |
| [ ] | 16 | [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) | 🟡 Medium | Parentheses validation |
| [ ] | 17 | [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) | 🟡 Medium | Balance counting |
| [ ] | 18 | [856. Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/) | 🟡 Medium | Nested structure evaluation |

**Concept checklist**

- [ ] Reverse Polish Notation
- [ ] Operator precedence
- [ ] Nested brackets and encoded strings
- [ ] Greedy decisions using a stack
- [ ] Simulating push/pop sequences

**Notes / mistakes to revisit:**

```text

```

---

## Phase 3 — Monotonic Stack

**Goal:** Master next/previous greater and smaller elements, monotonic ordering, and contribution techniques.

| Done | # | LeetCode Problem | Difficulty | Pattern / Focus |
|:--:|--:|:--|:--:|:--|
| [ ] | 19 | [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | 🟡 Medium | Next greater element |
| [ ] | 20 | [503. Next Greater Element Ii](https://leetcode.com/problems/next-greater-element-ii/) | 🟡 Medium | Circular next greater |
| [ ] | 21 | [901. Online Stock Span](https://leetcode.com/problems/online-stock-span/) | 🟡 Medium | Previous greater element |
| [ ] | 22 | [1475. Final Prices With A Special Discount In A Shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/) | 🟡 Medium | Next smaller element |
| [ ] | 23 | [907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) | 🟡 Medium | Monotonic stack + contribution |
| [ ] | 24 | [2104. Sum of Subarray Ranges](https://leetcode.com/problems/sum-of-subarray-ranges/) | 🟡 Medium | Subarray min/max contribution |
| [ ] | 25 | [1856. Maximum Subarray Min-Product](https://leetcode.com/problems/maximum-subarray-min-product/) | 🟡 Medium | Prefix sum + monotonic stack |
| [ ] | 26 | [853. Car Fleet](https://leetcode.com/problems/car-fleet/) | 🟡 Medium | Sorting + stack |
| [ ] | 27 | [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | 🔴 Hard | Previous/next smaller |
| [ ] | 28 | [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) | 🔴 Hard | Histogram + monotonic stack |
| [ ] | 29 | [2281. Sum of Total Strength of Wizards](https://leetcode.com/problems/sum-of-total-strength-of-wizards/) | 🔴 Hard | Contribution + prefix sums |
| [ ] | 30 | [456. 132 Pattern](https://leetcode.com/problems/132-pattern/) | 🟡 Medium | Reverse monotonic stack |

**Concept checklist**

- [ ] Monotonic increasing stack
- [ ] Monotonic decreasing stack
- [ ] Next Greater / Next Smaller Element
- [ ] Previous Greater / Previous Smaller Element
- [ ] Circular arrays
- [ ] Contribution technique
- [ ] Correct handling of duplicates and strict inequalities

**Notes / mistakes to revisit:**

```text

```

---

## Phase 4 — Advanced Stack Patterns

**Goal:** Apply stacks to iterators, parsing, greedy string construction, and complex simulations.

| Done | # | LeetCode Problem | Difficulty | Pattern / Focus |
|:--:|--:|:--|:--:|:--|
| [ ] | 31 | [232. Implement Queue Using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | 🟢 Easy | Two-stack queue |
| [ ] | 32 | [636. Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions/) | 🟡 Medium | Call-stack simulation |
| [ ] | 33 | [341. Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) | 🟡 Medium | Nested iterator |
| [ ] | 34 | [385. Mini Parser](https://leetcode.com/problems/mini-parser/) | 🟡 Medium | Parsing nested data |
| [ ] | 35 | [1717. Maximum Score From Removing Substrings](https://leetcode.com/problems/maximum-score-from-removing-substrings/) | 🟡 Medium | Greedy + stack |
| [ ] | 36 | [1963. Minimum Number Of Swaps To Make The String Balanced](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/) | 🟡 Medium | Parentheses imbalance |
| [ ] | 37 | [2434. Using a Robot to Print the Lexicographically Smallest String](https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/) | 🟡 Medium | Greedy + stack |
| [ ] | 38 | [1081. Smallest Subsequence of Distinct Characters](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/) | 🟡 Medium | Monotonic stack + frequency |
| [ ] | 39 | [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/) | 🟡 Medium | Expression parsing |
| [ ] | 40 | [1762. Buildings With an Ocean View](https://leetcode.com/problems/buildings-with-an-ocean-view/) | 🔴 Hard | Monotonic scan / stack |

**Concept checklist**

- [ ] Implementing a queue using stacks
- [ ] Nested iterators and parsers
- [ ] Greedy string construction
- [ ] Nested expressions and signs

**Notes / mistakes to revisit:**

```text

```

---

## Phase 5 — Queue & Deque Fundamentals

**Goal:** Understand FIFO, both-end operations, circular buffers, and queue simulation.

| Done | # | LeetCode Problem | Difficulty | Pattern / Focus |
|:--:|--:|:--|:--:|:--|
| [ ] | 41 | [933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) | 🟢 Easy | Queue + time window |
| [ ] | 42 | [2073. Time Needed to Buy Tickets](https://leetcode.com/problems/time-needed-to-buy-tickets/) | 🟢 Easy | Queue simulation |
| [ ] | 43 | [1700. Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/) | 🟢 Easy | Queue simulation |
| [ ] | 44 | [346. Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) | 🟢 Easy | Queue + rolling average |
| [ ] | 45 | [622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) | 🟡 Medium | Circular queue |
| [ ] | 46 | [641. Design Circular Deque](https://leetcode.com/problems/design-circular-deque/) | 🟡 Medium | Circular deque |
| [ ] | 47 | [649. Dota2 Senate](https://leetcode.com/problems/dota2-senate/) | 🟡 Medium | Queue + simulation |
| [ ] | 48 | [950. Reveal Cards In Increasing Order](https://leetcode.com/problems/reveal-cards-in-increasing-order/) | 🟡 Medium | Queue simulation |

**Concept checklist**

- [ ] FIFO principle
- [ ] collections.deque operations: append, appendleft, pop, popleft
- [ ] Circular queue and circular deque
- [ ] Front/rear pointer management
- [ ] Queue simulation

**Notes / mistakes to revisit:**

```text

```

---

## Phase 6 — Sliding Window + Deque

**Goal:** Combine sliding windows with deques to maintain useful candidates efficiently.

| Done | # | LeetCode Problem | Difficulty | Pattern / Focus |
|:--:|--:|:--|:--:|:--|
| [ ] | 49 | [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | 🟡 Medium | Two monotonic deques |
| [ ] | 50 | [1696. Jump Game Vi](https://leetcode.com/problems/jump-game-vi/) | 🟡 Medium | DP + monotonic deque |
| [ ] | 51 | [1823. Find the Winner of the Circular Game](https://leetcode.com/problems/find-the-winner-of-the-circular-game/) | 🟡 Medium | Circular queue |
| [ ] | 52 | [1670. Design Front Middle Back Queue](https://leetcode.com/problems/design-front-middle-back-queue/) | 🟡 Medium | Two deques |
| [ ] | 53 | [1429. First Unique Number](https://leetcode.com/problems/first-unique-number/) | 🟡 Medium | Queue + frequency map |
| [ ] | 54 | [2810. Faulty Keyboard](https://leetcode.com/problems/faulty-keyboard/) | 🟡 Medium | Deque / reverse construction |
| [ ] | 55 | [2762. Continuous Subarrays](https://leetcode.com/problems/continuous-subarrays/) | 🟡 Medium | Monotonic deques |
| [ ] | 56 | [362. Design Hit Counter](https://leetcode.com/problems/design-hit-counter/) | 🟡 Medium | Queue + time window |

**Concept checklist**

- [ ] Maintaining a maximum candidate with a decreasing deque
- [ ] Maintaining a minimum candidate with an increasing deque
- [ ] Removing expired indices from the front
- [ ] Removing dominated candidates from the back
- [ ] Using a deque to optimize sliding-window DP

**Notes / mistakes to revisit:**

```text

```

---

## Phase 7 — Advanced Monotonic Deque

**Goal:** Solve advanced window optimization and prefix-sum problems with a monotonic deque.

| Done | # | LeetCode Problem | Difficulty | Pattern / Focus |
|:--:|--:|:--|:--:|:--|
| [ ] | 57 | [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | 🟡 Medium | Monotonic decreasing deque |
| [ ] | 58 | [862. Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | 🔴 Hard | Prefix sum + monotonic deque |
| [ ] | 59 | [838. Push Dominoes](https://leetcode.com/problems/push-dominoes/) | 🟡 Medium | Queue / simulation |
| [ ] | 60 | [2398. Maximum Number of Robots Within Budget](https://leetcode.com/problems/maximum-number-of-robots-within-budget/) | 🔴 Hard | Sliding window + monotonic deque |

**Concept checklist**

- [ ] Sliding Window Maximum in O(n)
- [ ] Shortest subarray with negative numbers present
- [ ] Prefix sums + monotonic deque
- [ ] Combining a running maximum with a sliding-window cost constraint

**Notes / mistakes to revisit:**

```text

```

---

## 🧠 Pattern Recognition Cheat Sheet

| If the problem says... | Think... |
|:--|:--|
| Matching brackets or nested parentheses | Stack |
| Undoing or reversing recent operations | Stack / LIFO |
| Evaluate an expression or nested encoding | Stack |
| Next greater or next smaller element | Monotonic Stack |
| Previous greater or previous smaller element | Monotonic Stack |
| Largest rectangle in a histogram | Monotonic Stack |
| Contribution of each element to subarray minimums/maximums | Monotonic Stack |
| Process items in arrival order | Queue / FIFO |
| Add/remove from both ends | Deque |
| Maintain a maximum in a sliding window | Monotonic Decreasing Deque |
| Maintain a minimum in a sliding window | Monotonic Increasing Deque |
| Shortest subarray with sum at least K, including negative values | Prefix Sum + Monotonic Deque |

---

## ⭐ Tier 1 — MUST SOLVE

Prioritize these problems if you cannot complete all 60 immediately:

1. 20. Valid Parentheses
2. 155. Min Stack
3. 150. Evaluate Reverse Polish Notation
4. 394. Decode String
5. 735. Asteroid Collision
6. 739. Daily Temperatures
7. 907. Sum of Subarray Minimums
8. 84. Largest Rectangle in Histogram
9. 85. Maximal Rectangle
10. 239. Sliding Window Maximum
11. 862. Shortest Subarray with Sum at Least K
12. 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
13. 1696. Jump Game VI
14. 2398. Maximum Number of Robots Within Budget

---

## 📝 Daily Practice Method

For each problem:

### Step 1 — Identify the pattern

Before coding, ask:

```text
1. Does the problem involve last-in, first-out behavior?
2. Does it involve first-in, first-out behavior?
3. Do I need to inspect or remove elements from both ends?
4. Am I searching for the next/previous greater or smaller element?
5. Can a monotonic structure discard elements that can never be answers?
6. Is there a sliding window whose minimum or maximum must be maintained?
```

### Step 2 — Write the brute-force idea

```text
Brute Force
O(n²) or the natural straightforward approach
```

Then ask: *what repeated work can a stack, queue, or deque remove?*

### Step 3 — Derive the optimized pattern

```text
Brute Force
    ↓
Identify the required order
    ↓
Stack / Queue / Deque
    ↓
Monotonic Stack or Monotonic Deque (when needed)
```

### Step 4 — Code

Only code after you can explain what each stored element represents and why it is safe to remove an element.

### Step 5 — Re-solve

At the beginning of each study session, spend 10–15 minutes re-solving one previous problem without looking at your old code.

---

## 📊 Daily Problem-Solving Log

| Date | Problem # | Problem Name | Time Taken | Hints Used? | Solved Independently? | Key Learning |
|:--|--:|:--|:--:|:--:|:--:|:--|
| YYYY-MM-DD | | | | No / Yes | Yes / No | |
| YYYY-MM-DD | | | | No / Yes | Yes / No | |
| YYYY-MM-DD | | | | No / Yes | Yes / No | |
| YYYY-MM-DD | | | | No / Yes | Yes / No | |
| YYYY-MM-DD | | | | No / Yes | Yes / No | |

## 🔁 Revisit Tracker

Mark a problem if you needed a hint, viewed the solution, or could not explain the approach clearly.

| Problem # | Problem | First Attempt | Revisit Date | Solved Without Help? |
|--:|:--|:--:|:--:|:--:|
| | | | | |
| | | | | |
| | | | | |

---

## 🎯 Rules for This Roadmap

1. Attempt each problem before reading hints or editorials.
2. Start with a brute-force solution when possible; then derive the optimized approach.
3. Record time and space complexity.
4. Explain why the stack/deque invariant is correct.
5. For monotonic stack problems, identify exactly what each stack entry represents.
6. For monotonic deque problems, explain why elements can be removed from the front and back.
7. Re-solve problems that required hints after 2–3 days.
8. Do not move to the next phase until you can explain the current phase's core patterns.

---

## 🐍 Python Reference

```python
# Stack: list is suitable for LIFO operations
stack = []
stack.append(10)
top = stack[-1]
value = stack.pop()

# Queue / Deque: efficient operations at both ends
from collections import deque

dq = deque()
dq.append(10)        # Add to right
dq.appendleft(20)    # Add to left
right = dq.pop()     # Remove from right
left = dq.popleft()  # Remove from left

# Inspect both ends
front = dq[0]
back = dq[-1]
```

---

**🏆 Final goal:** Complete all 60 problems, understand the underlying invariants, and recognize when a Stack, Monotonic Stack, Queue, or Monotonic Deque is the right tool.

**🚀 Master the pattern, not the problem.**
