import os
import kubernetes.client as k8s


envs = [
    {"name": "HTTPS_PROXY", "value": os.environ["HTTPS_PROXY"]},
    {"name": "https_proxy", "value": os.environ["HTTPS_PROXY"]},
]


def create_git_clone_init_container(
    repo: str,
    branch: str
):
    return k8s.V1Container(
        name="clone-repo",
        image=os.getenv("CLONE_REPO_IMAGE", "navikt/knada-git-sync:2020-10-23-98963f6"),
        volume_mounts=[
            k8s.V1VolumeMount(
                name="dags-data", mount_path="/repo", sub_path=None, read_only=False
            ),
            k8s.V1VolumeMount(
                name="git-clone-secret",
                mount_path="/keys",
                sub_path=None,
                read_only=False,
            ),
        ],
        env=envs,
        command=["/bin/sh", "/git-clone.sh"],
        args=[repo, branch, "/repo"],
    )
