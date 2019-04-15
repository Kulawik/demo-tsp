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

