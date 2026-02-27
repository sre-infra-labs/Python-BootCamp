# Python Bootcamp

# Install pyenv to work with multiple python versions in different projects
```
# switch to repo directory
cd ~/Github/Python-Bootcamp

# ensure os packages are latest - https://github.com/pyenv/pyenv?tab=readme-ov-file#homebrew-in-macos
brew update
brew install pyenv

# setup shell environment - https://github.com/pyenv/pyenv?tab=readme-ov-file#b-set-up-your-shell-environment-for-pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init - zsh)"' >> ~/.zshrc
```

# Instal Jupyter Notebook
```
# switch to repo directory
cd ~/Github/Python-Bootcamp

# create virtual environment
python -m venv .venv

# active virtual env
source ./.venv/bin/activate

# install jupyter lab
pip install jupyterlab ipython rich

# start jupyter lab
jupyter lab
or
jupyter lab --notebook-dir="/path/to/your/directory"

```

# Find running notebook sessions
```
jupyter server list

|------------$ jupyter server list
Currently running servers:
http://ryzen9:8888/?token=067f39526afcbebef45e811479ffccb1c29757e846ee5c03 :: /home/saanvi
```


# Interview Preparation
- [Youtube - 50 Most Asked Python Interview Questions](https://www.youtube.com/watch?v=WH_ieAsb4AI)
- [Blog - Datacamp - Top Python Interview Questions](https://www.datacamp.com/blog/top-python-interview-questions-and-answers)
- 