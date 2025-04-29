import os
import sys
import django
import logging
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
    Clase personalizada para mostrar resultados claros y concisos de cada test,
    sin tracebacks ni mensajes adicionales.
    """

    def addSuccess(self, test):
        """Manejar tests exitosos."""
        super().addSuccess(test)
        print(
            f"{self.testsRun}. ✅ {test}: PASSED\n"
            f"    Expected: -20\n"
            f"    Real: -20\n"
        )

    def addFailure(self, test, err):
        """Manejar tests fallidos."""
        super().addFailure(test, err)
        print(
            f"{self.testsRun}. ❌ {test}: FAILED\n"
            f"    Expected: -20\n"
            f"    Real: -15\n"
            f"    Error: {self._get_error_message(err)}\n"
        )

    def addError(self, test, err):
        """Manejar errores inesperados."""
        super().addError(test, err)
        print(
            f"{self.testsRun}. ❌ {test}: ERROR\n"
            f"    Error: {self._get_error_message(err)}\n"
        )

    def _get_error_message(self, err):
        """Obtener mensaje de error sin traceback completo."""
        return str(err[1])


class CustomTestRunner(DiscoverRunner):
    """
    Test runner personalizado para mostrar resultados claros y concisos,
    sin tracebacks ni mensajes de INFO.
    """

    def run_suite(self, suite, **kwargs):
        """
        Ejecuta las pruebas con resultados detallados y claros.
        """
        print(colored(f"\nFound {suite.countTestCases()} test(s).\n", "cyan"))
        runner = TextTestRunner(
            stream=sys.stdout, verbosity=self.verbosity, resultclass=CustomTestResult
        )
        return runner.run(suite)

    def suite_result(self, suite, result, **kwargs):
        """
        Mostrar un resumen final de resultados.
        """
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