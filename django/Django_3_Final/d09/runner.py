import os
import sys
import django
import logging
from django.test.runner import DiscoverRunner
from termcolor import colored
from unittest import TextTestRunner, TextTestResult

# Cambia esto si tu settings module tiene otro nombre
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "d09.settings")
django.setup()

# Opcional: suprime mensajes de INFO de tus modelos
logging.getLogger("account.models").setLevel(logging.WARNING)

class CustomTestResult(TextTestResult):
    """
    TestResult personalizado que muestra solo el estado y la descripción de cada test.
    """

    def addSuccess(self, test):
        super().addSuccess(test)
        doc = test.shortDescription() or ""
        print(
            colored(f"{self.testsRun}. ✅ {test}: PASSED", "green")
            + (f"\n    Descripción: {doc}\n" if doc else "\n")
        )

    def addFailure(self, test, err):
        super().addFailure(test, err)
        doc = test.shortDescription() or ""
        print(
            colored(f"{self.testsRun}. ❌ {test}: FAILED", "red")
            + (f"\n    Descripción: {doc}\n" if doc else "\n")
            + f"    Error: {self._get_error_message(err)}\n"
        )

    def addError(self, test, err):
        super().addError(test, err)
        doc = test.shortDescription() or ""
        print(
            colored(f"{self.testsRun}. ❌ {test}: ERROR", "yellow")
            + (f"\n    Descripción: {doc}\n" if doc else "\n")
            + f"    Error: {self._get_error_message(err)}\n"
        )

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
    # Cambia 'account.tests' por la ruta a tu módulo de tests si es diferente
    test_runner = CustomTestRunner(verbosity=2)
    failures = test_runner.run_tests(["account.tests"])
    sys.exit(bool(failures))
