# Ramsey Number Searcher

A Ramsey Number is defined as $R(\Gamma)$ such that
$$n < R(\Gamma), n \nleftarrow \Gamma$$
$$n \geq R(\Gamma), n \leftarrow \Gamma$$


An algorithm to solve for a Ramsey Number $R(\Gamma)$ is 
$$
    RNS: \mathcal{P}(\mathbb{G}) \times \mathcal{P}(\mathbb{N}) \rightarrow \mathcal{P}(C(K_n) \cup \{ \varepsilon \})
$$
where $\mathbb{G}$ is the set of all graphs, and $C(K_n)$ is the set of all colorings.

RNS therefore takes as input a set of graphs $\Gamma$, and a set of (preferrably ordered) numbers $N$ and returns a graph coloring $c(K_n)$ or emptry string $\varepsilon$ for each $n \in N$.


## Usage

### Build

```bash
git submodule update --recursive --init
mkdir build
cmake -S . -B build/
cd build
make
```

### Running RNS

```bash
cd build
make rns
rns "[<graph_1>, <graph_2>, <graph_3>, ...]" "[<number_1>, <number_2>, <number_3>]"
```

alternatively

```bash
cd build
make rns
rns "file/path/to/description/file"
```

### Ramsey Description Files

A description file is a text file that describes a Ramsey Number problem.
It is included mostly for ease of running code on the same problem i.e. benchmarking / testing.

_Format_
```
graphs = [ <graph_1>, <graph_2>, <graph_3>, ... ]
numbers = [ <number_1>, <number_2>, <number_3>, ... ]
expected_answer = [ <number_1 arrows graphs counterexample>, <number_2 arrows graphs counterexample>, ... ]
```

The expected_answer values are ignored, but added to the file for convenience of viewing

### Benchmarks

The benchmarks return a formatted set of data that includes the execution time and input parameters of each benchmark.
RNS can be decomposed into the two subproblems ARW and USIP, these problems also have provided benchmarks

_Raw output format of benchmarks_

1. RNS - `list of graphs, list of numbers, list of output graphs, execution time (milliseconds)`
2. ARW - `searched number, list of graphs, output graph, execution time (milliseconds)`
3. USIP - `unfinished colored graph, colored subgraph, execution time (milliseconds)`

Some processing scripts will be provided to process the raw data into more readable formats.