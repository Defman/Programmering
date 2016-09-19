import inspect
import timeit


def test(fn):
    def run(*args, **kwargs):
        return fn(*args, **kwargs)
    return run

def timeit(times=1):
    def timeit_decorator(func):
        def func_wrapper(**kwargs)



class TestResult(object):
    def __init__(self, o1, o2, success, error):
        self.o1 = o1
        self.o2 = o2
        self.success = success
        self.error = error

    def __str__(self):
        return self.message if self.success else self.error


class TestCase(object):
    def assertEqual(self, o1, o2, success, error):
        return TestResult(o1, o2, o1 == o2, success, error)

    def assertNotEqual(self, o1, o2, error):
        return TestResult(o1, o2, o1 != o2, error)

    def assertIs(self, o1, o2, success, error):
        return TestResult(o1, o2, o1 is o2, success, error)

    def assertIsNot(self, o1, o2, success, error):
        return TestResult(o1, o2, o1 is not o2, success, error)

    def assertIn(self, o1, o2, success, error):
        return TestResult(o1, o2, o1 in o2, success, error)

    def assertNotIn(self, o1, o2, success, error):
        return TestResult(o1, o2, o1 not in o2, success, error)

    def assertGreater(self, o1, o2, success, error):
        return TestResult(o1, o2, o1 > o2, success, error)

    def assertNotGreater(self, o1, o2, success, error):
        return TestResult(o1, o2, not o1 > o2, success, error)

    def assertLess(self, o1, o2, success, error):
        return TestResult(o1, o2, o1 < o2, success, error)

    def assertNotLess(self, o1, o2, success, error):
        return TestResult(o1, o2, not o1 < o2, success, error)

    def get_tests(self):
        return map(lambda m: inspect.signature(m), inspect.getmembers(self, inspect.ismethod))

    def run(self):
        results = []
        for test in tests:
            result += test()

    def __str__(self):
        return str(self.get_tests())


class Foo(TestCase):
    @test
    def quadratic(self):
        self.assertEqual(1, 1, "it worked", "some error")

    def test(self):
        return str(inspect.signature(self))

print(Foo().test())