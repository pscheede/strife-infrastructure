import subprocess
from pathlib import Path

class StrifeBackend:
    @staticmethod
    def ensure_started():
        docker_compose_path = Path(__file__).parent / "strife-backend/docker-compose.yml"
        subprocess.run(
            ["sudo", "docker", "compose", "-f", str(docker_compose_path), "up", "-d"],
        )

    @staticmethod
    def stop():
        docker_compose_path = Path(__file__).parent / "strife-backend/docker-compose.yml"
        subprocess.run(
            ["sudo", "docker", "compose", "-f", str(docker_compose_path), "stop"],
        )
