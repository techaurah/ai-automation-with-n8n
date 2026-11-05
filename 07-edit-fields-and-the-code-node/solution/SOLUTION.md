# Lesson 07: Solution notes

The refactored version wins the midnight test for a concrete reason: when the urgent flag is wrong, you open exactly one small node whose input and output isolate the bug, instead of bisecting a forty-line script by commenting lines out. The long-word count belongs in the Code node (it is a loop over tokens with a condition); the trim and case work belongs in Edit Fields where a non-programmer teammate can verify it.

**What to notice.** "Identical output on three enquiries" was the real exercise. Refactors in automation are safe exactly when you can prove the before and after agree, and the habit of building the comparison first is worth more than either node.
