from typing import NamedTuple

import kfp
from kfp import dsl
import kfp.dsl as dsl

from kfp.components import func_to_container_op, InputPath, OutputPath



@component
def add(a: float, b: float) -> float:
  '''Calculates sum of two arguments'''
  return a + b


MY_BUCKET = "gs://my-pipeline-root/example-pipeline"


@dsl.pipeline(
  name='addition-pipeline',
  description='An example pipeline that performs addition calculations.',
  pipeline_root=MY_BUCKET
)

def add_pipeline(
  a: float=1,
  b: float=7,
):
  # Passes a pipeline parameter and a constant value to the `add` factory
  # function.
  first_add_task = add(a, 4)
  # Passes an output reference from `first_add_task` and a pipeline parameter
  # to the `add` factory function. For operations with a single return
  # value, the output reference can be accessed as `task.output` or
  # `task.outputs['output_name']`.
  second_add_task = add(first_add_task.output, b)

# Specify pipeline argument values
arguments = {'a': 7, 'b': 8}


client.create_run_from_pipeline_func(
    add_pipeline,
    arguments=arguments,
    mode=kfp.dsl.PipelineExecutionMode.V2_COMPATIBLE)




### 2
from typing import NamedTuple

@component(base_image='tensorflow/tensorflow:1.11.0-py3')
def my_divmod(
  dividend: float,
  divisor: float,
  metrics: Output[Metrics]) -> NamedTuple(
    'MyDivmodOutput',
    [
      ('quotient', float),
      ('remainder', float),
    ]):
    '''Divides two numbers and calculate  the quotient and remainder'''

    # Import the numpy package inside the component function
    import numpy as np

    # Define a helper function
    def divmod_helper(dividend, divisor):
        return np.divmod(dividend, divisor)

    (quotient, remainder) = divmod_helper(dividend, divisor)

    # Export two metrics
    metrics.log_metric('quotient', float(quotient))
    metrics.log_metric('remainder', float(remainder))

    from collections import namedtuple
    divmod_output = namedtuple('MyDivmodOutput',
        ['quotient', 'remainder'])
    return divmod_output(quotient, remainder)

### 3
import kfp.dsl as dsl
@dsl.pipeline(
   name='calculation-pipeline',
   description='An example pipeline that performs arithmetic calculations.',
   pipeline_root='gs://my-pipeline-root/example-pipeline'
)
def calc_pipeline(
   a: float=1,
   b: float=7,
   c: float=17,
):
    # Passes a pipeline parameter and a constant value as operation arguments.
    add_task = add(a, 4) # The add_op factory function returns
                            # a dsl.ContainerOp class instance. 

    # Passes the output of the add_task and a pipeline parameter as operation
    # arguments. For an operation with a single return value, the output
    # reference is accessed using `task.output` or
    # `task.outputs['output_name']`.
    divmod_task = my_divmod(add_task.output, b)

    # For an operation with multiple return values, output references are
    # accessed as `task.outputs['output_name']`.
    result_task = add(divmod_task.outputs['quotient'], c)


# Specify pipeline argument values
arguments = {'a': 7, 'b': 8}

# Submit a pipeline run
client.create_run_from_pipeline_func(
    calc_pipeline,
    arguments=arguments,
    mode=kfp.dsl.PipelineExecutionMode.V2_COMPATIBLE)