from django.test.runner import DiscoverRunner
from termcolor import colored

class CustomTestRunner(DiscoverRunner):
    def run_suite(self, suite, **kwargs):
        result = super().run_suite(suite, **kwargs)
        passed = result.testsRun - len(result.failures) - len(result.errors)
        failed = len(result.failures)
        errored = len(result.errors)
        print("\nResumen de pruebas:")
        print(colored(f"✅ {passed} pruebas pasaron", "green"))
        print(colored(f"❌ {failed} pruebas fallaron", "red"))
        print(colored(f"🟡 {errored} errores", "yellow"))
        return result

    def get_resultclass(self):
        from django.test.runner import DebugSQLTextTestResult

        class VerboseTestResult(DebugSQLTextTestResult):
            def addSuccess(self, test):
                doc = test.shortDescription() or ""
                print(colored(f"✅ {test._testMethodName}", "green"))
                if doc:
                    print(colored(doc, "green"))
                super().addSuccess(test)

            def addFailure(self, test, err):
                doc = test.shortDescription() or ""
                print(colored(f"❌ {test._testMethodName}", "red"))
                if doc:
                    print(colored(doc, "red"))
                super().addFailure(test, err)

            def addError(self, test, err):
                doc = test.shortDescription() or ""
                print(colored(f"🟡 {test._testMethodName}", "yellow"))
                if doc:
                    print(colored(doc, "yellow"))
                super().addError(test, err)

        return VerboseTestResult
