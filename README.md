# art-guesser


## Getting started
### Installing core dependencies
```sh
brew bundle
```
### Configuring ZSH to work with pyenv virtual env
```sh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
```
### Install python
```sh
pyenv install 3.10.3
```
### Set up virtual environment
```sh
pyenv virtualenv 3.10.3 ag
pyenv local ag
```