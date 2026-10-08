# Python Bootcamp

# Install pyenv to work with multiple python versions in different projects
```
# switch to repo directory
cd ~

# On Mac
  ## ensure os packages are latest - https://github.com/pyenv/pyenv?tab=readme-ov-file#homebrew-in-macos
  brew update
  brew install pyenv

  pyenv init --install

  ## setup shell environment - https://github.com/pyenv/pyenv?tab=readme-ov-file#b-set-up-your-shell-environment-for-pyenv
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
  echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
  echo 'eval "$(pyenv init - zsh)"' >> ~/.zshrc

# On Ubuntu
  ## Install pyenv with automatic installer
  curl -fsSL https://pyenv.run | bash

  ~/.pyenv/bin/pyenv init --install

# check installed python versions
pyenv versions

# install specific python version
pyenv install --list

pyenv install 3.14.3
pyenv install 3.11.15

pyenv versions

# Set global default (used everywhere)
pyenv global 3.14.3

# Set local version for a specific project folder
cd ~/my-project
pyenv local 3.11.15
python --version

# Set version for current shell session only
pyenv shell 3.11.15
python --version

```

# Instal Jupyter Notebook
```
# create virtual environment for jupyter notebook
cd ~
python -m venv .venv

# active virtual environment
source ~/.venv/bin/activate

# In virtual environment, install notebook
pip install notebook

# Launch notebook
jupyter notebook
 or
jupyter notebook /stale-storage/GitHub/Python-BootCamp

    http://localhost:8888/tree

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