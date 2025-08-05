# Exceptions and Assertions

**Unexpected Conditions**

- when procedure hits unexpected condition, get an exception, so like IndexError, TypeError, NameError etc.

# Handling Exceptions

- Usually cause an error and stop execution.
- Python can provide **handlers** for exceptions.

example:

try:
    # something
    # bad code
except:
    # do something to
    # handle problem

- if expressions in **try block all succedd**   
    - code continues after the except block
- Exceptions raised by any statement in the try body are handled in the excpet statement.
    - Execution continues with the body of the except statement
    - then other expressions after the block continue.

# Handle Specific Exceptions

- adding excpetion type after except (except ValueError:), makes it so that block specifically handles those errors.
- multiple except statements can be used to handle multiple types of exception.

# Other Blocks associated with Try Block

- else:
    - body of this is executed when all of try block is executed with no exception.
- finally:
    - always ran after try, else and except blocks even if error is raised or return break or continue are used.
    - good for clean-up code which should always run (like closing the file.)

# Raise 

- Using **raise** in except block manually raises an exception.

syntax:

raise ExceptionType("Optional Error Message")

- This stops execution and raises error.

- CUSTOM ERROR HANDLING

# Assertions: Defensive Programming Tool

- Used to raise an AssertionError if assumptions in docstring aren't met

syntax:
assert <statement that should be true>, "message if not true"

- used to stop execution right away if invalid inout out with what is requested is used.

# Assertions vs Exceptions

- Goal is to spot bugs ASAP and know why they occured
- **Exceptions** allow us to to handle unexpected input.
    - use when don't need to halt execution
    - raise exceptionsif users supply bad data input
- Use **Assertions**:
    - Enforce conditions on contract between coder and user.
    - supplement to testing
    - check types of arguments or values
    - check that invariants on data structures are met
    - check constraints on return values
    - check for violation of constraints on procedure.