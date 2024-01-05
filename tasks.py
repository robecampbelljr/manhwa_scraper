from invoke import task

@task
def install_requierments(ctx):
  ctx.run("pip install -r requirements.txt")