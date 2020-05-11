# Paquete de prueba de suma de numeros

Sum numbers.

## Installation

Apenas probando

## Usage

Install and call module sum

### Jupyter Notebook (formerly IPython)
We recommend generating reports interactively by using the Jupyter notebook.

To use pyspark with Jupyter, you must also set `PYSPARK_DRIVER_PYTHON`:

	export PYSPARK_DRIVER_PYTHON=/path/to/your/anaconda/bin/python

And then:

	IPYTHON_OPTS="notebook" /path/to/your/bin/pyspark

In `spark 2.0.X` `IPYTHON_OPTS` is removed: the environment variable you want to set is `PYSPARK_DRIVER_PYTHON_OPTS`:

	PYSPARK_DRIVER_PYTHON_OPTS="notebook" /path/to/your/bin/pyspark

Now you can create a new notebook, which will run pyspark.


To use spark-df-profiling, start by loading in your Spark DataFrame, e.g. by using

```python
# sqlContext is probably already created for you.
# To load a parquet file as a Spark Dataframe, you can:
df = sqlContext.read.parquet("/path/to/your/file.parquet")
# And you probably want to cache it, since a lot of 
# operations will be done while the report is being generated:
df_spark = df.cache()
```

To display the report in a Jupyter notebook, run:

```python
import prueba1
prueba1.add(numbers)
```

If you want to generate a HTML report file, save the ProfileReport to an object and use the `.to_file()` method:

```python
import prueba1
prueba1.add(numbers)
```

## Dependencies

* Python (`>=2.7`)
* Apache Spark (who would imagine!) -> requires Spark `>=1.5.0` (compatible with `2.0.0` also).
* **An internet connection.** spark-df-profiling requires an internet connection to download the Bootstrap and JQuery libraries. You can choose to embed them in the HTML template code, should you desire.
* jinja2 (`>=2.8`) -> needed for template rendering. Only needed in the Spark driver.
* matplotlib (`>=1.4`) -> needed for histogram creation. Only needed in the Spark driver.
* pandas (`>=0.17.0`) -> needed for internal data arrangement. Only needed in the Spark driver.
* six (`>=1.9.0`) -> needed for py2/3 compatibility. Only needed in the Spark driver.
* numpy (`>=1.18.1`) -> needed some functions.
