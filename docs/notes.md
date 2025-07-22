# Takeaways

## planning.md

-Think of my app, and what classes I might need to do what
-Build a class responsibility list, and then write tests for each class first, before writing the class
-Give each class a single responsibility, and separate concerns, only passing what I need
-Make sure I think about what each class needs to perform its job
-And that I pass valid values, making sure I use the correct data type (dict has problems with typos, use a class with attributes, or an enum,...)

-Start with TDD by picking one class that has no pdependencies and a clear in/output
-This class has one responsibility, and all tests should aim to make sure that it does its job and provides the downstream with the correct data / output
-So, for DataCleaner: job is to clean data, that means, does it work on a sin
-Each class should assume that the data it receives is already valid and processed correctly

-Fail fast! e.g. on DataCleaner, if a value is missing (required for Downstream), fail, and not clean immediately.

## Enum vs Dict:

-Dict keys are prone to typos, you can add accidental values if you mistype etc
-Enums are restricted to the values that I define initally + autocompletion of entries vs. (all possibilities of) dict keys
-Enum only represents the type (list of valid currencies), but does not store balances
-Have to associate currency.USD -> 50, so I need a mapping structure (like a dict) on top of the enum
-Enums are also immutable, so they can not be changed after the creation (no new currency type can be added at runtime)
-While a dict is mutable, so I can then add the value associated with that enum (mapped to it via dict)

## Type Safety:

-Only valid things are allowed
-Python would allow values like "many" (string) for the currencies, because it is a dynamically typed language

## Serialization:

-Means converting Python objects to a format like JSON, CSV (so it can be stored, displayed, or transferred)

## TDD:

-Red, Green, Refactor: Write a test_what_I_test() function in a test_classname.py, then use 'pytest' in the Terminal to run
-Red: minimal code to make the test fail (but fail in the desired manner, e.g. the underlying class / method is not defined)
-Green: write the minimal code to make the test pass, not more
-Refactor: then, rewrite the test

## Instance Method vs Class Method:

-Instance Method: def spend(self, amount, currency)
-Called on a specific instance of a class, can read / change that specific instance's state
-Class Method: @classmethod def spend(cls,...)
-Called on the class itself, and can not access self.balance (there is no self!)
