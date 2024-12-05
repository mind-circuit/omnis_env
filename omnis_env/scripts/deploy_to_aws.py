# omnis/scripts/deploy_to_aws.py

import subprocess
import os


def build_docker_image():
    subprocess.run(['docker', 'build', '-t', 'omnis_app', '.'])


def push_to_ecr():
    aws_account_id = os.getenv('AWS_ACCOUNT_ID')
    region = os.getenv('AWS_REGION')
    ecr_repo = f"{aws_account_id}.dkr.ecr.{region}.amazonaws.com/omnis_app"

    subprocess.run(['aws', 'ecr', 'get-login-password', '--region', region, '|',
                    'docker', 'login', '--username', 'AWS', '--password-stdin', ecr_repo])
    subprocess.run(['docker', 'tag', 'omnis_app:latest', f"{ecr_repo}:latest"])
    subprocess.run(['docker', 'push', f"{ecr_repo}:latest"])


def deploy_to_ecs():
    # Implement AWS ECS deployment steps or use AWS CLI
    pass


if __name__ == "__main__":
    build_docker_image()
    push_to_ecr()
    deploy_to_ecs()
