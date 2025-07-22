# Test-Driven Development (TDD) Checklist

## 1. Define the Class or Function Responsibility
- ✅ What is the single responsibility of this class/function?
- ✅ Can I describe it in one sentence?
- ✅ Is it leaking concerns that should belong elsewhere?

## 2. Design the Tests (Red Phase)

### A. Minimal Useful Behavior
- ✅ What is the smallest thing this class/function must do?

### B. Core Behavior Coverage
For each behavior:
- ✅ What is the expected input?
- ✅ What is the expected output?
- ✅ What errors can occur (wrong type, missing data, out of range)?
- ✅ Are any constraints involved (e.g., non-negative, valid enum)?

### C. Write the Tests
- ✅ Happy path: test correct inputs (using `assert`)
- ✅ Sad path: test incorrect inputs (using `with pytest.raises(...)`)

## 3. Write Minimal Implementation (Green Phase)
- ✅ Only write code to make the test pass.
- ✅ Avoid edge cases, abstractions, and refactoring.
- ✅ Focus on getting one test green.

## 4. Refactor (Refactor Phase)
- ✅ Rename variables, functions, parameters for clarity.
- ✅ Extract methods, deduplicate code.
- ✅ Add type hints and docstrings.
- ✅ Improve error messages.
- ✅ Ensure all tests still pass.

## 5. Repeat
- ✅ Add another test and iterate.
- ✅ Keep test suite green.

## TDD Best Practices
- ✅ Fail fast: validate inputs early.
- ✅ Raise explicit exceptions; no silent failures.
- ✅ Prefer one assert per test.
- ✅ Test behavior, not implementation.
- ✅ Refactor for clarity, not for performance.

---

This file can be included as `TDD_CHECKLIST.md` in the root of your GitHub repo.

