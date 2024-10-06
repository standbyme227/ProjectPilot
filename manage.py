# manage.py
import click
import json
import os
from subprocess import Popen
import psutil
import time

# 프로젝트 정보를 저장할 파일
PROJECTS_FILE = 'projects.json'

# 프로젝트 등록 함수
def load_projects():
    if os.path.exists(PROJECTS_FILE):
        with open(PROJECTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_projects(projects):
    with open(PROJECTS_FILE, 'w') as f:
        json.dump(projects, f, indent=4)

@click.group()
def cli():
    """CLI 프로그램"""
    pass

@cli.command()
@click.option('--name', prompt='Project name', help='The name of the project.')
@click.option('--path', prompt='Project path', help='The path of the project.')
@click.option('--command', prompt='Command to run', help='The command to execute.')
def add(name, path, command):
    """프로젝트를 등록"""
    projects = load_projects()
    projects.append({'name': name, 'path': os.path.abspath(path), 'command': command, 'status': 'Stopped'})
    save_projects(projects)
    click.echo(f"프로젝트 '{name}'이(가) 성공적으로 등록되었습니다.")

@cli.command()
def list():
    """등록된 프로젝트 리스트 보기"""
    projects = load_projects()
    if not projects:
        click.echo("등록된 프로젝트가 없습니다.")
        return

    for idx, project in enumerate(projects):
        click.echo(f"[{idx + 1}] {project['name']} - {project['status']}")

@cli.command()
@click.argument('name')
def start(name):
    """프로젝트 실행"""
    projects = load_projects()
    for project in projects:
        if project['name'] == name:
            if project['status'] == 'Running':
                click.echo(f"프로젝트 '{name}'이 이미 실행 중입니다.")
                return

            # 명령어 실행 (별도의 터미널에서 실행)
            log_file = open(f"{name}_log.txt", "w")
            error_file = open(f"{name}_error_log.txt", "w")
            process = Popen(project['command'], shell=True, cwd=project['path'], stdout=log_file, stderr=error_file)
            project['status'] = 'Running'
            project['pid'] = process.pid
            save_projects(projects)
            click.echo(f"프로젝트 '{name}'을(를) 실행했습니다.")
            return
    click.echo(f"프로젝트 '{name}'을(를) 찾을 수 없습니다.")

@cli.command()
@click.argument('name')
def stop(name):
    """프로젝트 종료"""
    projects = load_projects()
    for project in projects:
        if project['name'] == name:
            if project['status'] == 'Stopped':
                click.echo(f"프로젝트 '{name}'이 이미 중지되었습니다.")
                return

            # 프로세스 종료
            pid = project.get('pid')
            if pid and psutil.pid_exists(pid):
                process = psutil.Process(pid)
                process.terminate()
                project['status'] = 'Stopped'
                save_projects(projects)
                click.echo(f"프로젝트 '{name}'을(를) 중지했습니다.")
            else:
                click.echo(f"프로세스가 실행 중이 아닙니다.")
            return
    click.echo(f"프로젝트 '{name}'을(를) 찾을 수 없습니다.")

if __name__ == '__main__':
    cli()
