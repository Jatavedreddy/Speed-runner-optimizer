# Speed Runner Optimizer

A tool to demonstrate performance improvements using parallel processing.

## How to Run

### 1. Generate Data
First, generate the baseline data (200+ CSV files):
```bash
python generate_bulk_data.py
```

### 2. Run Comparison (Baseline vs Optimized)
To run both modes and see the speedup:
```bash
python optimizer.py --mode both
```

### 3. Run Individual Modes
**Baseline Mode:**
```bash
python optimizer.py --mode baseline
```

**Optimized Mode:**
```bash
python optimizer.py --mode optimized
```

## Choice of Parallelism: Multiprocessing
I chose **Multiprocessing** over Threading for this task. 
- **The Reason**: Data processing (calculating averages from CSV files) in Python is often limited by the Global Interpreter Lock (GIL). While reading files is I/O-bound, the parsing and mathematical operations performed by Pandas are CPU-intensive. Multiprocessing allows us to bypass the GIL and utilize multiple CPU cores, resulting in a significantly more noticeable speedup compared to threading.

## Generated Files
- `output/performance_results.json`: Contains the timing metrics and speedup calculation.

## Github Repository : 
```bash
https://github.com/Jatavedreddy/Speed-runner-optimizer
```