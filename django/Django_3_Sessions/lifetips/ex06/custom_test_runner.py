import os
import sys
import django
import logging
import inspect
from django.test.runner import DiscoverRunner
from termcolor import colored
from unittest import TextTestRunner, TextTestResult

# Configurar el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ex06.settings")
django.setup()

# Suprimir mensajes de INFO
logging.getLogger("tips.models").setLevel(logging.WARNING)

class CustomTestResult(TextTestResult):
    """
    TestResult personalizado que muestra la docstring y el código fuente de cada test.
    """

    def addSuccess(self, test):
        super().addSuccess(test)
        doc = test.shortDescription() or ""
        code = self._get_test_source(test)
        print(
            f"{self.testsRun}. ✅ {test}: PASSED\n"
            f"    Descripción: {doc}\n"
            f"    Código de comprobación:\n{code}\n"
        )

    def addFailure(self, test, err):
        super().addFailure(test, err)
        doc = test.shortDescription() or ""
        code = self._get_test_source(test)
        print(
            f"{self.testsRun}. ❌ {test}: FAILED\n"
            f"    Descripción: {doc}\n"
            f"    Código de comprobación:\n{code}\n"
            f"    Error: {self._get_error_message(err)}\n"
        )

    def addError(self, test, err):
        super().addError(test, err)
        doc = test.shortDescription() or ""
        code = self._get_test_source(test)
        print(
            f"{self.testsRun}. ❌ {test}: ERROR\n"
            f"    Descripción: {doc}\n"
            f"    Código de comprobación:\n{code}\n"
            f"    Error: {self._get_error_message(err)}\n"
        )

    def _get_test_source(self, test):
        try:
            method = getattr(test, test._testMethodName)
            return inspect.getsource(method)
        except Exception as e:
            return f"No se pudo obtener el código fuente: {e}"

    def _get_error_message(self, err):
        return str(err[1])

class CustomTestRunner(DiscoverRunner):
    def run_suite(self, suite, **kwargs):
        print(colored(f"\nFound {suite.countTestCases()} test(s).\n", "cyan"))
        runner = TextTestRunner(
            stream=sys.stdout, verbosity=self.verbosity, resultclass=CustomTestResult
        )
        return runner.run(suite)

    def suite_result(self, suite, result, **kwargs):
        total = result.testsRun
        failed = len(result.failures)
        errored = len(result.errors)
        passed = total - (failed + errored)

        print("\nResumen de pruebas:")
        print(colored(f"✅ {passed} pruebas pasaron", "green"))
        print(colored(f"❌ {failed} pruebas fallaron", "red"))
        print(colored(f"🟡 {errored} errores", "yellow"))
        return super().suite_result(suite, result, **kwargs)

if __name__ == "__main__":
    test_runner = CustomTestRunner(verbosity=2)
    failures = test_runner.run_tests(["tips.tests"])
    sys.exit(bool(failures))
