import requests
import zipfile
from pathlib import Path
import os

from apps.docker import StrifeBackend

def pull_strife_backend(asset_id: str):
    """Background task to pull new build artifacts from strife-backend CI workflow"""

    token = os.getenv('GH_TOKEN')
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {token}',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    url = f'https://api.github.com/repos/pscheede/strife-backend/actions/artifacts/{asset_id}/zip'
    response = requests.get(url, headers=headers, stream=True)
    response.raise_for_status()

    app_dir = Path(__file__).parent / 'strife-backend'
    artifact_path = app_dir / 'artifact.zip'

    with artifact_path.open('wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    old_jar_path = app_dir / 'app.jar'
    old_jar_path.unlink(missing_ok=True)

    with zipfile.ZipFile(artifact_path, 'r') as zip_ref:
        zip_ref.extractall(app_dir)

    artifact_path.unlink()

    StrifeBackend.stop()
    StrifeBackend.ensure_started()
