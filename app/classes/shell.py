import subprocess

class Shell:

    @staticmethod
    def build(name, user, password):
        subprocess.check_call(['./resources/shell_scripts/build.sh', name, user, password])

    @staticmethod
    def pull(name, user, password):
        subprocess.check_call(['./resources/shell_scripts/pull.sh', name, user, password])

    @staticmethod
    def remove(name, user, password):
        subprocess.check_call(['./resources/shell_scripts/remove.sh', name, user, password])

    @staticmethod
    def run(name, port, user, password):
        subprocess.check_call(['./resources/shell_scripts/run.sh', name, str(port), user, password])

    @staticmethod
    def stop(name, user, password):
        subprocess.check_call(['./resources/shell_scripts/stop.sh', name, user, password])
