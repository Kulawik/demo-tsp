# Traveling Salesman Problem Solver
The solver uses (Mu + Lambda) Evolutionary Algorithm from DEAP framework.

## Installing dependencies:
<pre><code>pipenv install</code></pre>

## Running tests:
<pre><code>pipenv run python -m pytest tspsolver</code></pre>
or
<pre><code>make test</code></pre>

## Running demo
with random vertices:
<pre><code>pipenv run python demo.py </code></pre>
or with specified input file:
<pre><code>pipenv run python demo.py -f ./data/dataset.tsv</code></pre>

### For more options refer to help page:
<pre><code>pipenv run python demo.py --help</code></pre>
```
usage: demo.py [-h] [--file FILE] [--vertices VERTICES] [--fast]
               [--generations GENERATIONS] [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  input file path
  --vertices VERTICES, -vert VERTICES
                        number of vertices to be genarated if no input file is
                        used
  --fast                use smaller population to shorten computation
  --generations GENERATIONS, -gen GENERATIONS
                        number of generations
  --verbose, -v         increase output verbosity
```
