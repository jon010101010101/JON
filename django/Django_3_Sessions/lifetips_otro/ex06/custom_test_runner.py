import os
import sys
import django
from django.test.runner import DiscoverRunner
from termcolor import colored
from unittest import TestResult

# Configurar el entorno de Django
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ex06.settings')


class CustomTestRunner(DiscoverRunner):
    """
    Test runner personalizado para:
    - Silenciar migraciones
    - Mostrar resultados con colores y puntos correctos
    - Proporcionar un resumen limpio al final
    """

    def setup_test_environment(self, **kwargs):
        """
        Configuración del entorno de pruebas, silenciando las migraciones.
        """
        super().setup_test_environment(**kwargs)
        from django.conf import settings
        settings.MIGRATION_MODULES = {
            app: None for app in settings.INSTALLED_APPS
        }

    def run_suite(self, suite, **kwargs):
        """
        Ejecuta las pruebas mostrando resultados con colores y numeración.
        """
        total_tests = suite.countTestCases()
        print(colored(f"Found {total_tests} test(s).", "cyan"))
        result = TestResult()

        for idx, test in enumerate(suite, start=1):
            # Captura el nombre descriptivo de la prueba
            test_description = self._get_test_description(test)

            try:
                # Ejecuta la prueba
                test.run(result)
                if result.wasSuccessful():
                    print(f"{idx}. {test_description} ... {colored('✅', 'green')}")
                else:
                    print(f"{idx}. {test_description} ... {colored('❌', 'red')}")
            except Exception as e:
                # Cambiar el error a un punto amarillo
                print(f"{idx}. {test_description} ... {colored('🟡', 'yellow')}")
                print(f"    {str(e)}")  # Mostrar el mensaje del error

        return result

    def _get_test_description(self, test):
        """
        Extrae la descripción de una prueba eliminando nombres técnicos.
        """
        full_name = str(test)
        # Ejemplo: "test_combination_of_votes (tips.tests.TipVoteTestCase)"
        start = full_name.find("Verificar")  # Buscar el inicio de la descripción
        if start != -1:
            return full_name[start:].strip()
        return full_name

    def suite_result(self, suite, result, **kwargs):
        """
        Mostrar un resumen final de resultados con colores.
        """
        total = result.testsRun
        failed = len(result.failures)
        errored = len(result.errors)
        passed = total - (failed + errored)

        print("\nResumen de pruebas:")
        print(colored(f"✅ {passed} pruebas pasaron", "green"))
        print(colored(f"❌ {failed} pruebas fallaron", "red"))
        print(colored(f"🟡 {errored} errores", "yellow"))  # Cambiar el resumen de errores a amarillo
        return super().suite_result(suite, result, **kwargs)


if __name__ == "__main__":
    django.setup()
    test_runner = CustomTestRunner(verbosity=2)
    failures = test_runner.run_tests(["tips.tests"])
    sys.exit(bool(failures))