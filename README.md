
---

# Week 1 Assignment: Introduction to Economic Attention Allocation (ECAN)

## Overview

This document outlines the process of testing, building, and running the **Economic Attention Allocation (ECAN)** system. It begins with writing unit and integration tests for various components of the ECAN system, ensuring thorough coverage of different functions. The building and running section details the steps needed to set up the ECAN system, including the installation and execution of the tests. The document also covers experiments with two agents interacting within the ECAN system, specifically focusing on how they influence attention allocation. Lastly, it describes the experiments conducted in the designated directory, which include testing the diffusion mechanism, verifying the propagation of STI values, and optimizing the system's overall performance.

---

## Test Cases for the Project

### 1. **Test Zero Diffusion**
**Goal**: Test edge cases where diffusion might be zero. This happens when the importance value (STI) or the diffusion percentage is zero.

```cpp
void ImportanceDiffusionUTest::testZeroDiffusion(void) {
    // Create a node with zero importance
    Handle src = _eval->eval_h("(Node \"A\")");
    AttentionBank& ab = attentionbank(_as);
    ab.stimulate(src, 0);  // Stimulate the node with 0 STI value

    AttentionValue::sti_t sti_before = get_sti(src);

    // Diffuse the atom
    _dmyid_agentptr->diffuseAtom(src);

    // Verify that the STI has not changed (should still be zero)
    TS_ASSERT_EQUALS(sti_before, get_sti(src)); // STI should remain 0
}
```

---

### 2. **Test for Correct Size of Diffusion Events**
**Goal**: Verify that the number of diffusion events is correct based on conditions like the number of atoms involved in the diffusion.

```cpp
void ImportanceDiffusionUTest::testSizeOfDiffusionEvents(void) {
    // Initialize a source node
    Handle src = _eval->eval_h("(Node \"A\")");
    AttentionBank& ab = attentionbank(_as);
    ab.stimulate(src, 50);  // Stimulate the node

    // Start diffusion process
    _dmyid_agentptr->diffuseAtom(src);

    // Check and debug the size of the diffusion stack
    std::stack<ImportanceDiffusionBase::DiffusionEventType> diffusionStack = _dmyid_agentptr->diffusionStack;
    std::cout << "Diffusion stack size: " << diffusionStack.size() << std::endl;

    // Assert the size of the stack is greater than 0
    TS_ASSERT(diffusionStack.size() > 0);
}
```

---

### 3. **Test Invalid Parameters**
```cpp
void AttentionParamQueryUTest::test_invalid_param() {
    // Attempt to get a value for a non-existent parameter
    TS_ASSERT_THROWS_ANYTHING(_atq.get_param_value("non-existent-param"));
}
```

---

### 4. **Test Numeric Edge Cases**
```cpp
void AttentionParamQueryUTest::test_numeric_edge_cases() {
    _atq.set_param("big-number", 1e9);
    TS_ASSERT_EQUALS("1000000000", _atq.get_param_value("big-number"));

    _atq.set_param("negative-number", -5);
    TS_ASSERT_EQUALS("-5", _atq.get_param_value("negative-number"));
}
```

---

### 5. **Test String Edge Cases**
```cpp
void AttentionParamQueryUTest::test_string_edge_cases() {
    _atq.set_param("empty-string", "");
    TS_ASSERT_EQUALS("", _atq.get_param_value("empty-string"));
}
```

---

### 6. **Test Duplicate Parameters**
```cpp
void AttentionParamQueryUTest::test_duplicate_params() {
    _atq.set_param("duplicate-param", 5);
    TS_ASSERT_EQUALS("5", _atq.get_param_value("duplicate-param"));

    // Set the same parameter with a new value
    _atq.set_param("duplicate-param", 10);
    TS_ASSERT_EQUALS("10", _atq.get_param_value("duplicate-param"));
}
```

---

### 7. **Test Boolean Parameters**
```cpp
void AttentionParamQueryUTest::test_boolean_params() {
    _atq.set_param("bool-true", true);
    TS_ASSERT_EQUALS("1", _atq.get_param_value("bool-true"));

    _atq.set_param("bool-false", false);
    TS_ASSERT_EQUALS("0", _atq.get_param_value("bool-false"));
}
```

---

## Building and Running the Project

Since I am using **Windows**, I found it helpful to use **VirtualBox** with **Xubuntu** to build and run the project. Below are the steps I followed to build and run the project:

### Steps:
```bash
git clone https://github.com/singnet/cogutil.git
cd cogutil
mkdir build
cd build
cmake ..
make
sudo make install

git clone --depth 1 https://github.com/singnet/atomspace.git
cd atomspace
mkdir build
cd build
cmake ..
make
sudo make install

git clone --depth 1 https://github.com/singnet/cogserver.git
cd cogserver
mkdir build
cd build
cmake ..
make -j
sudo make install

git clone --depth 1 https://github.com/singnet/attention.git
cd attention
mkdir build
cd build
cmake ..
make
sudo make install

make test
```


---
- Here is the output from running the tests **Before adding new tests**:

```bash
make test
```

```less
[  1%] Built target attention_atom_types
[  5%] Built target attention-types
[ 11%] Built target attentionval
[ 27%] Built target attentionbank
[ 53%] Built target attention
[ 55%] Generating HebbianCreationModuleUTest.cpp
[ 57%] Building CXX object tests/attention/CMakeFiles/HebbianCreationModuleUTest.dir/HebbianCreationModuleUTest.cpp.o
[ 59%] Linking CXX executable HebbianCreationModuleUTest
[ 59%] Built target HebbianCreationModuleUTest
[ 61%] Generating AttentionValueUTest.cpp
[ 62%] Building CXX object tests/attentionbank/CMakeFiles/AttentionValueUTest.dir/AttentionValueUTest.cpp.o
[ 64%] Linking CXX executable AttentionValueUTest
[ 64%] Built target AttentionValueUTest
[ 66%] Generating AttentionUTest.cpp
[ 68%] Building CXX object tests/attentionbank/CMakeFiles/AttentionUTest.dir/AttentionUTest.cpp.o
[ 70%] Linking CXX executable AttentionUTest
[ 70%] Built target AttentionUTest
[ 72%] Generating BankImplUTest.cpp
[ 74%] Building CXX object tests/attentionbank/CMakeFiles/BankImplUTest.dir/BankImplUTest.cpp.o
[ 75%] Linking CXX executable BankImplUTest
[ 75%] Built target BankImplUTest
[ 77%] Generating BankAsyncUTest.cpp
[ 79%] Building CXX object tests/attentionbank/CMakeFiles/BankAsyncUTest.dir/BankAsyncUTest.cpp.o
[ 81%] Linking CXX executable BankAsyncUTest
[ 81%] Built target BankAsyncUTest
[ 83%] Generating AttentionalFocusCBUTest.cpp
[ 85%] Building CXX object tests/attentionbank/CMakeFiles/AttentionalFocusCBUTest.dir/AttentionalFocusCBUTest.cpp.o
[ 87%] Linking CXX executable AttentionalFocusCBUTest
[ 87%] Built target AttentionalFocusCBUTest
[ 88%] Generating AttentionParamQueryUTest.cpp
[ 90%] Building CXX object tests/attention/CMakeFiles/AttentionParamQueryUTest.dir/AttentionParamQueryUTest.cpp.o
[ 92%] Linking CXX executable AttentionParamQueryUTest
[ 92%] Built target AttentionParamQueryUTest
[ 94%] Generating ImportanceDiffusionUTest.cpp
[ 96%] Building CXX object tests/attention/CMakeFiles/ImportanceDiffusionUTest.dir/ImportanceDiffusionUTest.cpp.o
[ 98%] Linking CXX executable ImportanceDiffusionUTest
[ 98%] Built target ImportanceDiffusionUTest
[ 98%] Built target tests
[100%] Running tests...
Test project /home/yohannes/Desktop/week_1_training_ECAN/attention/build/tests
    Start 1: AttentionValueUTest
1/9 Test #1: AttentionValueUTest ..............   Passed    0.10 sec
    Start 2: AttentionUTest
2/9 Test #2: AttentionUTest ...................   Passed    0.04 sec
    Start 3: BankImplUTest
3/9 Test #3: BankImplUTest ....................   Passed    0.02 sec
    Start 4: BankAsyncUTest
4/9 Test #4: BankAsyncUTest ...................   Passed    0.01 sec
    Start 5: AttentionalFocusCBUTest
5/9 Test #5: AttentionalFocusCBUTest ..........   Passed    1.25 sec
    Start 6: AttentionBankCythonTest
6/9 Test #6: AttentionBankCythonTest ..........***Failed    0.57 sec
Failure: ImportError (/usr/local/lib/opencog/librule.so: undefined symbol: _ZN7opencog15PREMISE_OF_LINKE) ... ERROR

======================================================================
ERROR: Failure: ImportError (/usr/local/lib/opencog/librule.so: undefined symbol: _ZN7opencog15PREMISE_OF_LINKE)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/nose/failure.py", line 39, in runTest
    raise self.exc_val.with_traceback(self.tb)
  File "/usr/lib/python3/dist-packages/nose/loader.py", line 416, in loadTestsFromName
    module = self.importer.importFromPath(
  File "/usr/lib/python3/dist-packages/nose/importer.py", line 47, in importFromPath
    return self.importFromDir(dir_path, fqname)
  File "/usr/lib/python3/dist-packages/nose/importer.py", line 94, in importFromDir
    mod = load_module(part_fqname, fh, filename, desc)
  File "/usr/lib/python3.10/imp.py", line 235, in load_module
    return load_source(name, filename, file)
  File "/usr/lib/python3.10/imp.py", line 172, in load_source
    module = _load(spec)
  File "<frozen importlib._bootstrap>", line 719, in _load
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/yohannes/Desktop/week_1_training_ECAN/attention/tests/attentionbank/cython/attentionbank_test.py", line 4, in <module>
    from opencog.type_constructors import *
ImportError: /usr/local/lib/opencog/librule.so: undefined symbol: _ZN7opencog15PREMISE_OF_LINKE

----------------------------------------------------------------------
Ran 1 test in 0.023s

FAILED (errors=1)

    Start 7: AttentionParamQueryUTest
7/9 Test #7: AttentionParamQueryUTest .........   Passed    0.31 sec
    Start 8: ImportanceDiffusionUTest
8/9 Test #8: ImportanceDiffusionUTest .........   Passed    0.43 sec
    Start 9: HebbianCreationModuleUTest
9/9 Test #9: HebbianCreationModuleUTest .......   Passed    1.76 sec

89% tests passed, 1 tests failed out of 9

Total Test time (real) =   4.52 sec

The following tests FAILED:
	  6 - AttentionBankCythonTest (Failed)
Errors while running CTest
make[3]: *** [CMakeFiles/test.dir/build.make:71: CMakeFiles/test] Error 8
make[2]: *** [CMakeFiles/Makefile2:398: CMakeFiles/test.dir/all] Error 2
make[1]: *** [CMakeFiles/Makefile2:405: CMakeFiles/test.dir/rule] Error 2
make: *** [Makefile:215: test] Error 2

```
---

- And Here is the output from running the tests **After adding the new tests**:

```bash
make test
```

```less
[  1%] Built target attention_atom_types
[  5%] Built target attention-types
[ 11%] Built target attentionval
[ 27%] Built target attentionbank
[ 53%] Built target attention
[ 59%] Built target HebbianCreationModuleUTest
[ 64%] Built target AttentionValueUTest
[ 70%] Built target AttentionUTest
[ 75%] Built target BankImplUTest
[ 81%] Built target BankAsyncUTest
[ 87%] Built target AttentionalFocusCBUTest
[ 88%] Generating AttentionParamQueryUTest.cpp
Consolidate compiler generated dependencies of target AttentionParamQueryUTest
[ 90%] Building CXX object tests/attention/CMakeFiles/AttentionParamQueryUTest.dir/AttentionParamQueryUTest.cpp.o
[ 92%] Linking CXX executable AttentionParamQueryUTest
[ 92%] Built target AttentionParamQueryUTest
[ 98%] Built target ImportanceDiffusionUTest
[ 98%] Built target tests
[100%] Running tests...
Test project /home/yohannes/Desktop/week_1_training_ECAN/attention/build/tests
    Start 1: AttentionValueUTest
1/9 Test #1: AttentionValueUTest ..............   Passed    0.08 sec
    Start 2: AttentionUTest
2/9 Test #2: AttentionUTest ...................   Passed    0.10 sec
    Start 3: BankImplUTest
3/9 Test #3: BankImplUTest ....................   Passed    0.07 sec
    Start 4: BankAsyncUTest
4/9 Test #4: BankAsyncUTest ...................   Passed    0.06 sec
    Start 5: AttentionalFocusCBUTest
5/9 Test #5: AttentionalFocusCBUTest ..........   Passed    0.52 sec
    Start 6: AttentionBankCythonTest
6/9 Test #6: AttentionBankCythonTest ..........***Failed    0.93 sec
Failure: ImportError (/usr/local/lib/opencog/librule.so: undefined symbol: _ZN7opencog15PREMISE_OF_LINKE) ... ERROR

======================================================================
ERROR: Failure: ImportError (/usr/local/lib/opencog/librule.so: undefined symbol: _ZN7opencog15PREMISE_OF_LINKE)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/nose/failure.py", line 39, in runTest
    raise self.exc_val.with_traceback(self.tb)
  File "/usr/lib/python3/dist-packages/nose/loader.py", line 416, in loadTestsFromName
    module = self.importer.importFromPath(
  File "/usr/lib/python3/dist-packages/nose/importer.py", line 47, in importFromPath
    return self.importFromDir(dir_path, fqname)
  File "/usr/lib/python3/dist-packages/nose/importer.py", line 94, in importFromDir
    mod = load_module(part_fqname, fh, filename, desc)
  File "/usr/lib/python3.10/imp.py", line 235, in load_module
    return load_source(name, filename, file)
  File "/usr/lib/python3.10/imp.py", line 172, in load_source
    module = _load(spec)
  File "<frozen importlib._bootstrap>", line 719, in _load
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/yohannes/Desktop/week_1_training_ECAN/attention/tests/attentionbank/cython/attentionbank_test.py", line 4, in <module>
    from opencog.type_constructors import *
ImportError: /usr/local/lib/opencog/librule.so: undefined symbol: _ZN7opencog15PREMISE_OF_LINKE

----------------------------------------------------------------------
Ran 1 test in 0.059s

FAILED (errors=1)

    Start 7: AttentionParamQueryUTest
7/9 Test #7: AttentionParamQueryUTest .........   Passed    2.24 sec
    Start 8: ImportanceDiffusionUTest
8/9 Test #8: ImportanceDiffusionUTest .........   Passed    0.23 sec
    Start 9: HebbianCreationModuleUTest
9/9 Test #9: HebbianCreationModuleUTest .......   Passed    1.30 sec

89% tests passed, 1 tests failed out of 9

Total Test time (real) =   5.55 sec

The following tests FAILED:
	  6 - AttentionBankCythonTest (Failed)
Errors while running CTest
make[3]: *** [CMakeFiles/test.dir/build.make:71: CMakeFiles/test] Error 8
make[2]: *** [CMakeFiles/Makefile2:398: CMakeFiles/test.dir/all] Error 2
make[1]: *** [CMakeFiles/Makefile2:405: CMakeFiles/test.dir/rule] Error 2
make: *** [Makefile:215: test] Error 2

```


---

## Writing Tests Considering Two Agents

### 1. **Test Diffusion with Different Node Types**
**Goal**: Test if the diffusion mechanism works for different types of nodes, such as regular nodes and more complex node types (e.g., `AsymmetricHebbianLink`, `InheritanceLink`).

```cpp
void ImportanceDiffusionUTest::testDiffusionWithDifferentNodeTypes(void) {
    // Create various node types
    Handle src = _eval->eval_h("(Node \"A\")");      // Regular node
    Handle target = _eval->eval_h("(Node \"Y\")");   // Another regular node
    Handle link = _eval->eval_h("(AsymmetricHebbianLink (Node \"X\") target (stv 0.6 0.9))");  // Link node

    AttentionBank& ab = attentionbank(_as);
    ab.stimulate(src, 50);  // Stimulate regular node
    ab.stimulate(target, 30);  // Stimulate another regular node
    ab.stimulate(link, 20);    // Stimulate a link node

    // Perform diffusion for each node
    _dmyid_agentptr->diffuseAtom(src);
    _dmyid_agentptr->diffuseAtom(target);
    _dmyid_agentptr->diffuseAtom(link);

    // Validate the diffusion effects
    TS_ASSERT(get_sti(src) > 50);       // Source node's STI should increase
    TS_ASSERT(get_sti(target) > 30);    // Target node's STI should increase
    TS_ASSERT(get_sti(link) > 20);      // Link node's STI should increase
}
```

---

## **Experiments Directory**

### **Objective of the Codebase in the Experiments Directory**
The **experiments directory** is designed to validate and refine the **ECAN (Economic Attention Allocation)** system in **OpenCog**, focusing on key functionalities related to cognitive modeling and attention allocation.

### **Primary Objective**
Validate and optimize the ECAN system to simulate human-like associative memory, allocate attention resources economically, and handle dynamic, evolving datasets.

### **Specific Objectives**
1. **Test HebbianLink Creation**:
   - Validate the formation of **HebbianLinks** between co-occurring atoms.
   - Model associative memory by strengthening links between related concepts.

2. **Verify STI Propagation**:
   - Ensure attention values propagate correctly through **HebbianLinks** and atoms within the **Attentional Focus**.

3. **Implement Forgetting Mechanisms**:
   - Introduce forgetting mechanisms based on thresholds to manage memory and computational resources.

4. **Simulate Cognitive Processes**:
   - Use **SentenceGenStimulateAgent** to simulate stimuli, allowing the system to process linguistic or conceptual input.

5. **Benchmark and Fine-Tune Parameters**:
   - Experiment with different configurations to optimize ECAN performance, such as STI funds, forgetting percentages, and HebbianLink diffusion.

---


### **NB:**
- During the project, I encountered a challenging issue with the test case "6 - AttentionBankCythonTest (Failed)" caused by the error:
`ImportError: /usr/local/lib/opencog/librule.so: undefined symbol: _ZN7opencog15PREMISE_OF_LINKE`.
The problem was related to importing `from opencog.type_constructors import *`, which was difficult to resolve.
- The aid of AI was used for preparing this document.
